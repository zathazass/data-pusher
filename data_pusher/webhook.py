# from django.contrib.auth import get_user_model
# User = get_user_model()
# user = User.objects.get(username="pydanny")

# from djwebhooks.models import Webhook
# WebhookTarget.objects.create(
#     owner=user,
#     event="purchase.paid",
#     target_url="https://mystorefront.com/webhooks/",
#     header_content_type=Webhook.CONTENT_TYPE_JSON,
# )

# from django.contrib.auth import get_user_model
# User = get_user_model()
# user = User.objects.get(username="pydanny")

# from djwebhooks.decorators import hook

# from myproject.models import Purchase

# # Event argument helps identify the webhook target
# @hook(event="purchase.paid")
# def send_purchase_confirmation(purchase, owner): # Webhook_owner also helps identify the webhook target
#     return {
#         "order_num": purchase.order_num,
#         "date": purchase.confirm_date,
#         "line_items": [x.sku for x in purchase.lineitem_set.filter(inventory__gt=0)]
#     }

# for purchase in Purchase.objects.filter(status="paid"):
#     send_purchase_confirmation(purchase=purchase, owner=user)