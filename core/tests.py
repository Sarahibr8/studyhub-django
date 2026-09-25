from django.test import TestCase


class StudyHubTests(TestCase):
    def test_home_and_resources_pages(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        self.assertEqual(self.client.get("/resources/").status_code, 200)
        self.assertEqual(self.client.get("/favorites/").status_code, 200)
        self.assertEqual(self.client.get("/preferences/").status_code, 200)
        self.assertEqual(self.client.get("/feedback/").status_code, 200)

    def test_resource_detail_and_custom_404(self):
        self.assertEqual(self.client.get("/resources/1/").status_code, 200)
        self.assertEqual(self.client.get("/resources/999/").status_code, 404)
        self.assertEqual(self.client.get("/this-page-does-not-exist/").status_code, 404)

    def test_favorites_add_and_remove(self):
        response = self.client.post(
            "/favorites/",
            {"action": "add", "resource_id": "1"},
        )
        self.assertRedirects(response, "/favorites/")

        response = self.client.get("/favorites/")
        self.assertContains(response, "Django URL Dispatcher Guide")

        response = self.client.post(
            "/favorites/",
            {"action": "remove", "resource_id": "1"},
        )
        self.assertRedirects(response, "/favorites/")

        response = self.client.get("/favorites/")
        self.assertNotContains(response, "Django URL Dispatcher Guide")

    def test_preferences_theme_change(self):
        response = self.client.post("/preferences/", {"theme": "dark"})
        self.assertRedirects(response, "/preferences/")
        self.assertEqual(response.cookies["theme"].value, "dark")

        response = self.client.get("/preferences/")
        self.assertContains(response, "Current theme: <strong>Dark</strong>")

    def test_feedback_validation_and_success(self):
        invalid = self.client.post(
            "/feedback/",
            {
                "name": "Sarah",
                "email": "sarah@example.com",
                "message": "Short",
                "rating": "5",
            },
        )
        self.assertEqual(invalid.status_code, 200)
        self.assertContains(invalid, "at least 10 characters")

        valid = self.client.post(
            "/feedback/",
            {
                "name": "Sarah",
                "email": "sarah@example.com",
                "message": "This is valid feedback.",
                "rating": "5",
            },
        )
        self.assertEqual(valid.status_code, 302)
        self.assertEqual(valid.url, "/feedback/thanks/")

        thanks = self.client.get("/feedback/thanks/")
        self.assertContains(thanks, "Thanks, Sarah.")
