import json
from pprint import pprint


def process(i):
    if i.get("category", "") != "login":
        print(f'Skiped: {i.get("category", "")}')
        return

    fields = i.get("fields", [])
    records = {}
    relate_fields = {
        "url": "URL",
        "username": "Username",
        "email": "Username",
        "phone": "Username",
        "password": "Password",
        "totp": "OTPAuth",
        "multiline": "Notes",
    }
    for j in fields:
        # print(j)
        if j.get("deleted", 0) != 0 or not j.get("value", ""):
            continue
        if j["type"] not in relate_fields:
            continue
        if relate_fields[j["type"]] not in records:
            records[relate_fields[j["type"]]] = j["value"].split(",")[0]
    records["Notes"] = records.get("Notes", "").replace("\n", " ")
    records["OTPAuth"] = records.get("OTPAuth", "").strip()
    records["Title"] = i.get("title", records.get("URL", ""))
    return records


def main():
    t = open("output.csv", "w+")
    t.write("Title,URL,Username,Password,Notes,OTPAuth\n")
    with open("enpass_export.json", "r") as f:
        pass_txt = f.read()
        pass_json = json.loads(pass_txt)
        for i in pass_json.get("items", []):
            try:
                records = process(i)
                if records:
                    t.write(
                        f"{records['Title']},{records.get('URL', '')},{records.get('Username', '')},{records['Password']},{records['Notes']},{records.get('OTPAuth', '')}\n"
                    )
            except Exception as e:
                if "android://" in records.get("URL", ""):
                    continue
                pprint(e)
                pprint(records)
                print(i)
                break


if __name__ == "__main__":
    main()
