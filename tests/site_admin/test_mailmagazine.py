import pytest

from app.site_admin.admin_profile.models import MailMagazine, MailMagazineReceiver


# test config
@pytest.mark.django_db
class TestMailMagazine:
    def test_create(self, create_mailmagazine):
        assert MailMagazine.objects.count() == 1

    def test_update(self, create_mailmagazine):
        mailmagazine = create_mailmagazine
        mailmagazine.type = "type update"
        mailmagazine.save()
        mailmagazine_test = MailMagazine.objects.get(id=mailmagazine.id)
        assert mailmagazine_test.type == "type update"

    def test_delete(self, create_mailmagazine):
        assert MailMagazine.objects.count() == 1
        create_mailmagazine.delete()
        assert MailMagazine.objects.count() == 0


@pytest.mark.django_db
class TestMailMagazineReceiver:
    def test_create(self, create_mail_magazine_receiver):
        assert MailMagazineReceiver.objects.count() == 1

    def test_update(self, create_mail_magazine_receiver):
        mail_magazine_receiver = create_mail_magazine_receiver
        mail_magazine_receiver.content = "content update"
        mail_magazine_receiver.save()
        mail_magazine_receiver_test = MailMagazineReceiver.objects.get(
            id=mail_magazine_receiver.id
        )
        assert mail_magazine_receiver_test.content == "content update"

    def test_delete(self, create_mail_magazine_receiver):
        assert MailMagazineReceiver.objects.count() == 1
        create_mail_magazine_receiver.delete()
        assert MailMagazineReceiver.objects.count() == 0
