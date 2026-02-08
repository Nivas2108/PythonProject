# 1. Design a Subscription class that:
# • Tracks how many total subscriptions have been created (shared across all users).
# • Allows each user to upgrade or downgrade their subscription using a function that
# depends on that user’s data only.
# • Provides a utility function that checks whether a given plan name is valid (e.g.,
# "Basic", "Pro", "Elite").
# • Should also provide a way to update the global discount percentage applied to all
# subscriptions at billing time.
# Create multiple subscriptions, validate various plan names, update the global
# discount, and show how billing changes for each user.
class Subscription:
    total_subscriptions = 0
    global_discount = 0  # percentage
    def __init__(self, user, plan):
        if not Subscription.is_valid_plan(plan):
            print("Invalid plan")
            return
        self.user = user
        self.plan = plan
        Subscription.total_subscriptions += 1
    def change_plan(self, new_plan):
        if Subscription.is_valid_plan(new_plan):
            self.plan = new_plan
        else:
            print("Invalid plan change")
    def calculate_bill(self):
        if self.plan == "Basic":
            price = 500
        elif self.plan == "Pro":
            price = 1000
        elif self.plan == "Elite":
            price = 1500
        discount = price * Subscription.global_discount / 100
        return price - discount
    @staticmethod
    def is_valid_plan(plan):
        return plan == "Basic" or plan == "Pro" or plan == "Elite"
    @classmethod
    def update_discount(cls, discount):
        cls.global_discount = discount
s1 = Subscription("Nivas", "Basic")
s2 = Subscription("Asha", "Pro")
print("Total subscriptions:", Subscription.total_subscriptions)
Subscription.update_discount(20)