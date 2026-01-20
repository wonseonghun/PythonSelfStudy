contacts = {}


def run():
    while True:  # 의미없는 거네.
        print("===연락처 관리 프로그램===")
        print("1. 추가 | 2. 검색 | 3. 삭제 | 4. 전체보기 | 5. 종료")
        menu = input("메뉴를 선택하세요 : ")

        if menu == "1":
            add_contacts()
        elif menu == "2":
            find_contacts()
        elif menu == "3":
            delete_contacts()
        elif menu == "4":
            print_contacts()
        elif menu == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")


def add_contacts():
    name = str(input("이름을 입력하세요 : "))
    phoneNumber = input("전화번호를 입력하세요 : ")
    #  contacts = {name: phoneNumber} 이건 틀림
    contacts[name] = phoneNumber


def print_contacts():
    for _name, _phoneNumber in contacts.items():
        print(f"{_name}의 전화번호는 {_phoneNumber}입니다.")


def find_contacts():
    print("검색 방법 : 1. 이름 | 2. 전화번호")
    menu_2 = input("검색 방법을 입력하세요 : ")

    if menu_2 == "1":
        name = input("이름을 작성하세요. : ")

        if name in contacts:
            print(f"{name}의 전화번호는 {contacts[name]}입니다.")
            return
        else:
            print("존재하지 않습니다.")
            return

    elif menu_2 == "2":
        _phonenumber = input("전화번호를 작성하세요 : ")
        for name, phonenumber in contacts.items():
            if _phonenumber == phonenumber:
                print(f"{name}의 전화번호는 {_phonenumber}입니다.")
                return

        print("존재하지 않습니다.")
        return

    else:
        print("잘못된 입력입니다.")


def delete_contacts():
    target_name = ""
    print("삭제할 방법 : 1. 이름 | 2. 전화번호")
    menu_3 = input("삭제 방법을 입력하세요 : ")
    if menu_3 == "1":
        name = input("이름을 작성하세요 :")

        if name in contacts:
            del contacts[name]  # 반복문 사용 중 삭제하면 에러 확률 높다.

        else:
            print("존재하지 않습니다.")
            return

    elif menu_3 == "2":
        _phonenumber = input("전화번호를 작성하세요 : ")
        for name, phonenumber in contacts.items():
            if _phonenumber == phonenumber:
                target_name = name
                break

        if target_name == "":  # 없다는 뜻.
            print("존재하지 않습니다.")
            return
        else:
            del contacts[target_name]


run()
