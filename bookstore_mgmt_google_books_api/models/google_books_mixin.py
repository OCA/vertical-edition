import base64
from datetime import datetime

import requests
import unidecode
from google_books_api_wrapper.api import GoogleBooksAPI

from odoo import _, models
from odoo.exceptions import UserError


class GoogleBooksMixin(models.AbstractModel):
    _name = "google.books.mixin"

    def get_convert_to_base64(self, url):
        return base64.b64encode(requests.get(url, timeout=5).content)

    def get_editorial_id(self, editorial_name):
        editorial_id = self.env["product.book.editorial"].search(
            [("name", "ilike", unidecode.unidecode(editorial_name))]
        )
        if not editorial_id:
            editorial_id = self.env["product.book.editorial"].create(
                {"name": editorial_name}
            )
        if len(editorial_id) > 1:
            editorial = editorial_id.filtered(lambda x: x.name == editorial_name)
            return editorial if editorial else editorial_id[0]
        return editorial_id

    def get_genre_id(self, genres):
        for genre_name in genres:
            genre_id = self.env["product.book.genre"].search(
                [("name", "ilike", unidecode.unidecode(genre_name))]
            )
            if not genre_id:
                genre_id = self.env["product.book.genre"].create({"name": genre_name})
            if len(genre_id) > 1:
                genre = genre_id.filtered(
                    lambda x, genre_name=genre_name: x.name == genre_name
                )
                return genre if genre else genre_id[0]
            return genre_id

    def get_author_id(self, author_name):
        author_id = self.env["product.book.author"].search(
            [("name", "ilike", unidecode.unidecode(author_name))]
        )
        if not author_id:
            author_id = self.env["product.book.author"].create({"name": author_name})
        if len(author_id) > 1:
            author = author_id.filtered(lambda x: x.name == author_name)
            return author if author else author_id[0]
        return author_id

    def action_import_from_isbn(self):
        for record in self.filtered(lambda x: x.is_book):
            if record.barcode:
                client = GoogleBooksAPI()
                isbn = record.barcode.replace("-", "")
                book = client.get_book_by_isbn13(isbn)
                if not book:
                    book = client.get_book_by_isbn10(isbn)
                if book:
                    # Set data to be updated
                    data = {
                        "name": book.title,
                    }

                    if book.published_date:
                        # Convert to year format
                        try:
                            published_year = datetime.strptime(
                                book.published_date, "%Y-%m-%d"
                            ).year
                        except Exception:
                            published_year = int(book.published_date[:4])

                        data["year_edition"] = published_year

                    if book.authors:
                        data["author_id"] = record.get_author_id(book.authors[0])

                    if book.publisher:
                        data["editorial_id"] = record.get_editorial_id(book.publisher)

                    if book.subjects:
                        data["genre_id"] = record.get_genre_id(book.subjects)

                    if book.description:
                        data["description"] = book.description
                        data["description_sale"] = book.description

                    if book.large_thumbnail:
                        data["image_1920"] = record.get_convert_to_base64(
                            book.large_thumbnail
                        )

                    # Update book data in Odoo
                    record.write(data)

                    # Show success notification
                    self.env.user.notify_success(
                        message=_("Book data updated from Google Books API")
                    )

                else:
                    # Return not found notification
                    return {
                        "type": "ir.actions.client",
                        "tag": "display_notification",
                        "params": {
                            "title": _("Warning"),
                            "type": "warning",
                            "message": _("Not book found with this data"),
                            "sticky": True,
                        },
                    }
            else:
                raise UserError(_("ISBN code is mandatory. Please, provide one."))
