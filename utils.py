def generate_user_id(env):    
    raw_name = env.get("FULL_NAME", "john_doe")
    dob = env.get("DOB", "17091999")
    normalized = raw_name.strip().lower().replace(" ", "_")
    return f"{normalized}_{dob}"


def process_array(body, env):
    user_id = generate_user_id(env)
    email = env.get("EMAIL", "john@xyz.com")
    roll_number = env.get("ROLL_NUMBER", "ABCD123")

    if not body or "data" not in body or not isinstance(body["data"], list):
        return {
            "is_success": False,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum": "0",
            "concat_string": ""
        }

    data = body["data"]
    odd_numbers, even_numbers, alphabets, special_characters = [], [], [], []
    concat_source = ""
    total_sum = 0

    for item in data:
        s = str(item)
        if s.isdigit():
            num = int(s)
            if num % 2 == 0:
                even_numbers.append(s)
            else:
                odd_numbers.append(s)
            total_sum += num
            continue
        if s.isalpha():
            alphabets.append(s.upper())
            concat_source += s
            continue
        special_characters.append(s)

   
    concat_string = ""
    if concat_source:
        reversed_chars = list(concat_source[::-1])
        for i, ch in enumerate(reversed_chars):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()

    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }
