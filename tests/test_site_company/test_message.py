import pytest

from app.site_company.message.models import Message, MessageTemplate, AutoReplyMessage


# test message
@pytest.mark.django_db
class TestMessage:
    def test_create(self, create_message):
        assert Message.objects.count() == 1

    def test_update(self, create_message):
        message = create_message
        message.body = "body update"
        message.save()

        message_test = Message.objects.get(id=message.id)
        assert message_test.body == "body update"

    def test_delete(self, create_message):
        assert Message.objects.count() == 1
        create_message.delete()
        assert Message.objects.count() == 0


# test message_template
@pytest.mark.django_db
class TestMessageTemplate:
    def test_create(self, create_message_template):
        assert MessageTemplate.objects.count() == 1

    def test_update(self, create_message_template):
        message_template = create_message_template
        message_template.name = "name update"
        message_template.save()

        message_template_test = MessageTemplate.objects.get(id=message_template.id)
        assert message_template_test.name == "name update"

    def test_delete(self, create_message_template):
        assert MessageTemplate.objects.count() == 1
        create_message_template.delete()
        assert MessageTemplate.objects.count() == 0


# test auto_reply_message
@pytest.mark.django_db
class TestAutoReplyMessage:
    def test_create(self, create_auto_reply_message):
        assert AutoReplyMessage.objects.count() == 1

    def test_update(self, create_auto_reply_message):
        auto_reply_message = create_auto_reply_message
        auto_reply_message.template_name = "template name update"
        auto_reply_message.save()

        auto_reply_message_test = AutoReplyMessage.objects.get(id=auto_reply_message.id)
        assert auto_reply_message_test.template_name == "template name update"

    def test_delete(self, create_auto_reply_message):
        assert AutoReplyMessage.objects.count() == 1
        create_auto_reply_message.delete()
        assert AutoReplyMessage.objects.count() == 0
