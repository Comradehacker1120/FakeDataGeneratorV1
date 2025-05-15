import random
import requests
from datetime import datetime
from typing import Dict

# ===== CONFIGURATION =====
CONFIG = {
    "telegram": {
        "bot_token": "",
        "chat_id": "",
        "enabled": False
    }
}

# ===== CULTURAL DATABASE =====
CULTURAL_DATA = {
    "Nigeria": {
        "ethnic_groups": {
            "Yoruba": {
    "first_names": [
        "Adeola", "Oluwaseun", "Tolulope", "Ademide", "Olabisi", "Adebayo", "Folake", "Femi", "Temitope", "Yetunde",
        "Segun", "Taiwo", "Kehinde", "Omotola", "Babatunde", "Sade", "Ayotunde", "Bolaji", "Muyiwa", "Titilayo",
        "Ifedayo", "Morounkeji", "Tunde", "Abiodun", "Akin", "Funmilayo", "Mobolaji", "Adewale", "Oluwatobi", "Iretiola",
        "Jubril", "Kemi", "Adedayo", "Tope", "Ranti"
    ],
    "last_names": [
        "Adeleke", "Ogunlesi", "Awolowo", "Iyabo", "Ojo", "Fagbemi", "Adeyemi", "Adesina", "Ajayi", "Alabi",
        "Bamidele", "Banjo", "Balogun", "Durojaiye", "Fashola", "Ige", "Ilori", "Ladipo", "Lawal", "Makinde",
        "Obasanjo", "Odumosu", "Ogundipe", "Olaniyan", "Olanrewaju", "Olatunji", "Olumide", "Omisore", "Oni", "Oyebanji",
        "Salako", "Shonibare", "Shoyinka", "Tinubu", "Yahaya"
    ],
    "cities": [
        "Lagos", "Ibadan", "Abeokuta", "Akure", "Osogbo", "Ilorin", "Ilesha", "Ijebu Ode", "Ogbomoso", "Oyo"
    ]
},

"Igbo": {
    "first_names": [
        "Chukwuemeka", "Ngozi", "Chiamaka", "Ifeanyi", "Chigozie", "Obinna", "Amaka", "Nkechi", "Uchechukwu", "Nnenna",
        "Somtochukwu", "Chioma", "Okechukwu", "Kelechi", "Nzube", "Ugochukwu", "Nkiru", "Onyeka", "Nwachinemere", "Ijeoma",
        "Ikenna", "Chisom", "Ebuka", "Ifunanya", "Nnaemeka", "Adaobi", "Uchenna", "Kosisochukwu", "Tochukwu", "Chizoba",
        "Chinonso", "Chidinma", "Chibuzo", "Onyinye", "Nkem"
    ],
    "last_names": [
        "Okonkwo", "Nwachukwu", "Eze", "Obi", "Uche", "Okafor", "Anyanwu", "Okezie", "Iwu", "Okorie",
        "Ezeugwu", "Madu", "Okeke", "Ezimora", "Nwosu", "Ewurum", "Nwankwo", "Ogu", "Omeje", "Onoh",
        "Nwoke", "Nwobodo", "Odili", "Ogbonna", "Onwuka", "Onyema", "Onyejekwe", "Onoh", "Okon", "Chukwu",
        "Orji", "Umeh", "Ibe", "Mbanaso", "Anyim"
    ],
    "cities": [
        "Enugu", "Owerri", "Onitsha", "Aba", "Awka", "Nsukka", "Abakaliki", "Nnewi", "Umuahia", "Orlu"
    ]
},

"Hausa": {
    "first_names": [
        "Ibrahim", "Amina", "Yusuf", "Fatima", "Habiba", "Musa", "Zainab", "Abubakar", "Umar", "Hauwa",
        "Sani", "Asabe", "Aliyu", "Maryam", "Shehu", "Aisha", "Kabiru", "Bilkisu", "Ahmad", "Rahila",
        "Isah", "Khadija", "Garba", "Lami", "Haruna", "Sa'adatu", "Tijjani", "Zuwaira", "Nasiru", "Bala",
        "Rabi", "Yahaya", "Bilkisu", "Idris", "Bashir"
    ],
    "last_names": [
        "Mohammed", "Musa", "Abubakar", "Sani", "Hassan", "Umar", "Garba", "Isah", "Kabir", "Aliyu",
        "Bello", "Abdullahi", "Aminu", "Tukur", "Lawan", "Dikko", "Maikudi", "Yusuf", "Shehu", "Zubairu",
        "Usman", "Bukar", "Iliyasu", "Rabiu", "Danjuma", "Muktar", "Suleiman", "Tijjani", "Nasir", "Faruk",
        "Ibrahim", "Bashir", "Idris", "Yakubu", "Nuhu"
    ],
    "cities": [
        "Kano", "Kaduna", "Sokoto", "Zaria", "Gusau", "Katsina", "Bauchi", "Birnin Kebbi", "Maiduguri", "Yola"
    ]
            }
        },
        "banks": [
    "GTBank", "Zenith Bank", "Access Bank", "First Bank", "UBA", "Union Bank", "Fidelity Bank", "Sterling Bank",
    "Keystone Bank", "Wema Bank", "EcoBank", "Polaris Bank", "Heritage Bank", "Providus Bank", "Stanbic IBTC"
],
        "phone_format": "+234 {}{}{} {}{}{} {}"

    },
    "United Kingdom": {
        "ethnic_groups": {
            "English": {
    "first_names": [
        "Oliver", "Charlotte", "Jack", "Emily", "Harry", "Amelia", "George", "Isla", "Noah", "Ava",
        "Leo", "Mia", "Oscar", "Grace", "Jacob", "Lily", "Thomas", "Sophie", "Henry", "Evie",
        "Alfie", "Ella", "Freddie", "Poppy", "Charlie", "Isabella", "Theo", "Rosie", "James", "Daisy",
        "Archie", "Ruby", "Sebastian", "Hannah", "Samuel", "Millie", "Lucas", "Florence", "Finley", "Jessica"
    ],
    "last_names": [
        "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Davies", "Evans", "Thomas", "Johnson",
        "Roberts", "Walker", "Wright", "Robinson", "Thompson", "White", "Hughes", "Edwards", "Green", "Hall",
        "Wood", "Harris", "Clarke", "Lewis", "Lee", "Turner", "Scott", "Hill", "Baker", "Adams",
        "Morris", "Mitchell", "Ward", "Carter", "Phillips", "Parker", "Anderson", "James", "Watson", "Young"
    ],
    "cities": [
        "London", "Manchester", "Birmingham", "Liverpool", "Leeds", "Sheffield", "Bristol", "Nottingham", "Leicester", "Coventry",
        "Newcastle", "Southampton", "Reading", "Portsmouth", "Derby", "Plymouth", "Wolverhampton", "York", "Oxford", "Cambridge"
    ]
            }
        },
        "banks": ["HSBC", "Barclays", "NatWest", "Lloyds"],
        "phone_format": "+44 7{}{} {}{}{} {}{}{}"
    }
}

# ===== CREDIT CARD GENERATOR =====
class CreditCardGenerator:
    BIN_DATABASE = {
    "Nigeria": {
        "Visa": [
            "400000", "402635", "409999", "428485", "419740", "439188", "453978", "455633",
            "471364", "474503", "484783", "485620", "486050"
        ],
        "Mastercard": [
            "510012", "512345", "519999", "521083", "523456", "525276", "526456", "529999",
            "535989", "536353", "538103", "539983", "558888"
        ],
        "Verve": [
            "506099", "506199", "506103", "507865", "507850", "507882", "650002", "650045",
            "650029", "507881", "628051", "628052"
        ]
        },
        "International": {
    "Visa": [
        "400000", "401288", "402400", "403550", "409999", "411111", "421765", "422222", "428485", "453291",
        "455673", "456789", "459999", "470012", "471610", "474503", "484783", "486010", "491660", "499999"
    ],
    "Mastercard": [
        "510510", "511111", "512345", "513456", "514785", "515735", "516789", "518765", "519999", "520082",
        "521234", "522222", "523456", "524000", "525555", "526456", "528001", "529999", "550000", "552188"
    ],
    "Amex": [
        "340000", "341111", "342345", "343434", "344444", "345678", "346789", "347981", "348888", "349999",
        "370000", "371234", "372345", "373737", "374562", "375675", "376888", "377777", "378282", "379999"
    ]
        }
    }

    @staticmethod
    def generate(country: str, card_type: str, vbv: bool = False) -> Dict[str, str]:
        # Verve is only available for Nigeria
        if card_type == "Verve" and country != "Nigeria":
            print("\nVerve cards are only available for Nigeria. Defaulting to Visa.")
            card_type = "Visa"
            
        bins = CreditCardGenerator.BIN_DATABASE.get(country, {}).get(
            card_type, CreditCardGenerator.BIN_DATABASE["International"].get(card_type))
        
        if not bins:
            print(f"\n{card_type} not available for {country}. Defaulting to Visa.")
            bins = CreditCardGenerator.BIN_DATABASE["International"]["Visa"]
        
        # Generate card number
        if len(bins) == 1:  # Single digit prefix
            card_number = bins[0] + "".join([str(random.randint(0,9)) for _ in range(15)])
        else:  # Full BIN
            card_number = bins[1] + "".join([str(random.randint(0,9)) for _ in range(12)])
        
        # Luhn check
        card_number = CreditCardGenerator._apply_luhn(card_number)
        
        return {
            "number": " ".join([card_number[i:i+4] for i in range(0, len(card_number), 4)]),
            "expiry": f"{random.randint(1,12):02d}/{datetime.now().year % 100 + random.randint(1,5)}",
            "cvv": f"{random.randint(100,999):03d}",
            "type": card_type,
            "vbv": "Enabled" if vbv else "Disabled",
            "country": country
        }

    @staticmethod
    def _apply_luhn(number: str) -> str:
        """Apply Luhn algorithm to make number valid"""
        total = 0
        for i, digit in enumerate(reversed(number)):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n = (n % 10) + 1
            total += n
        check = (10 - (total % 10)) % 10
        return number[:-1] + str(check)

# ===== PROFILE GENERATOR =====
class ProfileGenerator:
    @staticmethod
    def generate(country: str, ethnic_group: str = None) -> Dict[str, str]:
        if country not in CULTURAL_DATA:
            country = "Nigeria"
        
        ethnic_groups = list(CULTURAL_DATA[country]["ethnic_groups"].keys())
        if not ethnic_group or ethnic_group not in ethnic_groups:
            ethnic_group = random.choice(ethnic_groups)
        
        group_data = CULTURAL_DATA[country]["ethnic_groups"][ethnic_group]
        first_name = random.choice(group_data["first_names"])
        last_name = random.choice(group_data["last_names"])
        
        email = f"{first_name.lower()}{last_name.lower()}{random.randint(10,99)}@example.com"
        phone = ProfileGenerator._format_phone(CULTURAL_DATA[country]["phone_format"])
        
        return {
            "country": f"{country} ({ethnic_group})",
            "name": f"{first_name} {last_name}",
            "email": email,
            "phone": phone,
            "address": f"{random.randint(1,999)} {random.choice(['Street', 'Avenue', 'Road'])}",
            "city": random.choice(group_data["cities"]),
            "dob": f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/{datetime.now().year - random.randint(18,60)}",
            "bank": random.choice(CULTURAL_DATA[country]["banks"]),
            "ethnicity": ethnic_group
        }

    @staticmethod
    def _format_phone(format_str: str) -> str:
        parts = []
        for placeholder in format_str.split("{}"):
            if placeholder:
                parts.append(placeholder)
            parts.append("".join([str(random.randint(0, 9)) for _ in range(random.randint(3, 4))]))
        return "".join(parts)

# ===== MAIN APPLICATION =====
def show_menu():
    print("\n" + "="*50)
    print("🔥CMDHCK ULTIMATE FAKE DATA GENERATOR 🔥".center(50))
    print("="*50)
    print("\n1. Generate Profile")
    print("2. Generate Credit Card")
    print("3. Generate Full Identity (Profile + CC)")
    print("4. Configure Telegram")
    print("5. Exit")
    return input("\nSelect option: ").strip()

def select_country():
    print("\nSelect Country:")
    countries = list(CULTURAL_DATA.keys())
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")
    while True:
        try:
            choice = int(input("\nSelect: "))
            if 1 <= choice <= len(countries):
                return countries[choice-1]
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a number.")

def select_ethnic_group(country):
    print("\nSelect Ethnic Group:")
    groups = list(CULTURAL_DATA[country]["ethnic_groups"].keys())
    for i, group in enumerate(groups, 1):
        print(f"{i}. {group}")
    while True:
        try:
            choice = input("\nSelect (0 for random): ").strip()
            if choice == "0":
                return None
            choice = int(choice)
            if 1 <= choice <= len(groups):
                return groups[choice-1]
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a number.")

def select_card_type():
    print("\nSelect Card Type:")
    types = ["Visa", "Mastercard", "Verve"]
    for i, type in enumerate(types, 1):
        print(f"{i}. {type}")
    while True:
        try:
            choice = int(input("\nSelect: "))
            if 1 <= choice <= len(types):
                return types[choice-1]
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    print("\nInitializing Fake Data Generator...")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            country = select_country()
            ethnic_group = select_ethnic_group(country)
            
            profile = ProfileGenerator.generate(country, ethnic_group)
            print("\nGenerated Profile:")
            for key, value in profile.items():
                print(f"{key.title()}: {value}")
            
            if CONFIG["telegram"]["enabled"]:
                if input("\nSend to Telegram? (y/n): ").lower() == "y":
                    pass
        
        elif choice == "2":
            country = select_country()
            card_type = select_card_type()
            vbv = input("Enable VBV? (y/n): ").lower() == "y"
            
            cc = CreditCardGenerator.generate(country, card_type, vbv)
            print("\nGenerated Card:")
            for key, value in cc.items():
                print(f"{key.title()}: {value}")
        
        elif choice == "3":
            country = select_country()
            ethnic_group = select_ethnic_group(country)
            card_type = select_card_type()
            vbv = input("Enable VBV? (y/n): ").lower() == "y"
            
            print("\nGenerating complete identity...")
            profile = ProfileGenerator.generate(country, ethnic_group)
            cc = CreditCardGenerator.generate(country, card_type, vbv)
            
            print("\n=== PROFILE ===")
            for key, value in profile.items():
                print(f"{key.title()}: {value}")
            
            print("\n=== CREDIT CARD ===")
            for key, value in cc.items():
                print(f"{key.title()}: {value}")
        
        elif choice == "4":
            CONFIG["telegram"]["enabled"] = input("Enable Telegram? (y/n): ").lower() == "y"
            if CONFIG["telegram"]["enabled"]:
                CONFIG["telegram"]["bot_token"] = input("Enter bot token: ")
                CONFIG["telegram"]["chat_id"] = input("Enter chat ID: ")
        
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()