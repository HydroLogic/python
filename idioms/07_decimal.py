from decimal import Decimal # Arbitrary-precision floating point

# https://en.wikipedia.org/wiki/Floating_point
1.00 # Potentially imprecise but faster because its operations are in hardware
Decimal('1.00') # Precise but slower because its operations are in software
