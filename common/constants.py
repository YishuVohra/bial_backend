class Choices(object):
	'''
	Class to return choice options
	'''
	gender_choices = (
	    ('male', 'Male'),
	    ('female', 'Female'),
	    ('other', 'Other')
	)


class UserGroup:
    AREA_MANAGER = "area manager"
    SALES_MANAGER = "sales manager"
    REGIONAL_MANAGER = "REGIONAL manager"
    AGENT = "agent"


class ResponseConstants:
    STATUS_CODES  = {
        "AGENT_100": "Admin created ",    # Rohit K.
        "AGENT_101": "Agent created ",
        "AGENT_102": "Agent approved ",
        "AGENT_103": "Agents listed ",
        "AGENT_104": "Incorrect KYC details",
        "AGENT_105": "Incorrect Address details",
        "AGENT_106": "Agent not found ",
        "AGENT_107": "Field error for Agent",
        "AGENT_108": "Employee Files Saved",
        "AGENT_109": "Agent disapproved ",
        "AGENT_110": "Invalid referral code ",
        "AGENT_111": "Invalid reporting person ",
        "AGENT_112": "Invalid company ",
        "AGENT_113": "Profile with this code already exists",
        "AGENT_114": "Employee code successfully updated",
        
        # Country codes
        "COUNTRY_101": "Country created",
        "COUNTRY_102": "Country already exists for given name",
        "COUNTRY_103": "Invalid payload to create country",
        "COUNTRY_104": "Countries listed successfully",

        # STATE codes
        "STATE_101": "State created",
        "STATE_102": "State already exists for given name",
        "STATE_103": "Invalid payload to create state",
        "STATE_104": "States listed successfully",

        # City codes
        "CITY_101": "City created",
        "CITY_102": "City already exists for given name",
        "CITY_103": "Invalid payload to create City",
        "CITY_104": "Cities listed successfully",

        "PINCODE_101": "Invalid pincode",
        "PINCODE_102": "Pincode details successfully listed",

        # user codes
        "USER_101": "User mobile number already exists",
        "USER_102": "User email already exists",
        "USER_103": "User username already exists",

        #bank codes
        "BANK_102" : "Incorrect bank details",
        "BANK_101" : "Invalid Bank Name",

        # KYC codes:
        "KYC_101": "Pan number already exists",
        "KYC_102": "Adhar number already exists",
        "KYC_103": "Incorrect qualification",

        #OTP codes:
        "OTP_101": "Invalid OTP",
        "OTP_102": "OTP verified",
        "OTP_103": "Maximum number of attempts reached. Please try again after sometime",
        "OTP_104": "This number is already registered.",
        "OTP_105": "OTP generated successfully"

    }

