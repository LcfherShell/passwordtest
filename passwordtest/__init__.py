"""
Source code By: @LcfherShell (2023)
email: LcfherShell@tutanota.com
"""
try:
    from passwordtest.main import PasswordTest, PasswordStrength, Threadser, Version
    from passwordtest.PassCLI import Mainprogram
except:
    from main import PasswordTest, Version
    from PassCLI import Mainprogram

__all__ = ["PasswordTest", "PasswordStrength", "Threadser", "Version"]
