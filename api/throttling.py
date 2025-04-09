from rest_framework.throttling import UserRateThrottle

class Jackratethrottle(UserRateThrottle):
    scope='jack'