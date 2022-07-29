class User :    # 클래스를 지정하는 방법 중의 하나 : PascalCase(단어 시작에 대문자), camelCase(둘째 단어부터 대문자), snakecase(단어 중간에 _)
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # 팔로우, 팔로잉 함수
        user.followers += 1
        self.following += 1


user_1 = User('001', 'hajun')
user_2 = User('002', 'jack')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

