# Calculating Damage
# Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time
# Return "invalid" if damage or speed is negative.


def damage(damage, speed, time):
    if speed < 0 or damage < 0:
        return "invalid"
    if time == "second":
        return damage * speed
    if time == "minute":
        return damage * speed * 60
    if time == "hour":
        return damage * speed * 3600


# def damage(damage, speed, time):
#     if speed < 0 or damage < 0:
#         return "invalid"
#     if time == "second":
#         return damage * speed
#     if time == "minute":
#         return damage * speed * 60
#     if time == "hour":
#         return damage * speed * 3600


# def damage(damage, speed, time):
#     total_time = convert_time(time)
#     total_speed = speed * total_time
#     total_damage = damage * total_speed
#
#     if damage < 0:
#         print('invalid')
#         return 'invalid'
#
#     if speed < 0:
#         print('invalid')
#         return 'invalid'
#
#     print(f'total damage is {total_damage}')
#     return total_damage
#
#
# def convert_time(time):
#     if time is "second":
#         return 1
#
#     if time is "minute":
#         return 60
#
#     if time is "hour":
#         return 3600
#

# Examples
damage(100, 1, "minute") # , 6000)
damage(2, 100, "hour") # , 720000)
damage(20, 0.5, "minute") # , 600)
damage(2, 400, "hour") # , 2880000)
damage(-23, 20, "second") # , "invalid")
damage(-23, -5, "second") # , "invalid")
damage(20, -492321, "hour")  # , "invalid")


# def convert_time(speed, time):
#     time_in_seconds = speed
#
#     if time is "minute":
#         return speed * 60
#
#     if time is "hour":
#         return speed * 360
#
#     return time_in_seconds * speed

