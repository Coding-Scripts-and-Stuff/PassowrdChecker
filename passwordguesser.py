#is your password secure??
#from nordpass 200 most popular passwords

#imports
import time
#waring
print("WARNING, just because your password may not in this list does not mean it is secure/good")
#wait 2 secs
time.sleep(2)
#gets password
password = input('enter passsword: ')
#password list
passowords = ['123456', '123456789', 'picture1', 'password', '12345678', '111111', '123123', '12345', '1234567890', 'senha', '1234567', 'qwerty', 'abc123', 'Million2' ,'000000', '1234', 'iloveyou', 'maaron431' ,'password1' ,'qqww1122', '123', 'omgpop', '123321', '654321', 'qwertyuiop', 'qwer123456', '123456a', 'a123456', '666666', 'asdfghjkl', 'unknown', 'zxcvbnm', '112233', 'chatbooks', '20100728', '123123123', 'princess', 'jacket025', 'evite', '123abc', '123qwe', 'sunshine', '121212', 'dragon', '5201314', '159753', '123456789', 'pokemon', 'qwerty123', 'Bangbang123', 'jobandtalent', 'monkey', '1qaz2wsx', 'abcd1234', 'default', 'aaaaaa', 'soccer', '123654', 'ohmnamah23', '12345678910', 'zing', 'shadow', '102030', '11111111', 'asdfgh', '147258369', 'qazwsx', 'qwe123', 'michael', 'football', 'baseball', '1q2w3e4r5t', 'party', 'daniel', 'asdasd', '222222', 'myspace1', 'asd123', '555555', 'a123456789', '888888', '7777777', 'fuckyou', '1234qwer', 'superman', '147258', '999999', '159357', 'love123', 'tigger', 'purple', 'samantha', 'charlie', 'babygirl', '88888888', 'jordan23', '789456123', 'jordan', 'anhyeuem', 'killer', 'basketball', 'michelle', '1q2w3e', 'lol123', 'qwerty1', '789456', '6655321', 'nicole', 'naruto', 'master', 'chocolate', 'maggie', 'computer', 'hannah', 'jessica', '123456789', 'password123', 'hunter', '686584', 'iloveyou1', '987654321', 'justin', 'cookie', 'hello', 'blink182', 'andrew', '25251325', 'love', '987654', 'bailey', 'princess1', '123456', '101010', '12341234', 'a801016', '1111', '111111', 'anthony', 'yugioh', 'fuckyou1', 'amanda', 'asdf1234', 'trustno1', 'butterfly', 'x4ivygA51F', 'iloveu', 'batman', 'starwars', 'summer', 'michael1', '00000000', 'lovely', 'jakcgt333', 'buster', 'jennifer', 'babygirl1', 'family', '456789', 'azerty', 'andrea', 'q1w2e3r4', 'qwer1234', 'hello123', '10203', 'matthew', 'pepper', '12345a', 'letmein', 'joshua', '131313', '123456b', 'madison', 'Sample123', '777777', 'football1', 'jesus1', 'taylor', 'b123456', 'whatever', 'welcome', 'ginger', 'flower', '333333', '1111111111', 'robert', 'samsung', 'a12345', 'loveme', 'gabriel', 'alexander', 'cheese', 'passw0rd', '142536', 'peanut', '11223344', 'thomas', 'angel1Password', 'xxxxxx', '11111111', 'turtle', 'rainbow', 'parker', 'jessie', '123456', 'welcome', 'thx1138', 'sophie', 'gunner', 'topgun', 'shelby', '12345678', 'james', 'marlboro', 'danielle', '987654', 'asdfasdf', 'chevy', '1234', 'player', 'zxcvbnm', 'redskins', 'freddy', 'heavos', 'qwerty', 'ncc1701', 'panther', 'toyota', 'alexis', 'animal', 'airborne', '12345', 'wizard', 'redsox', 'jason', '2112', 'bigboy', 'dragon', 'scooby', 'victoria', 'sierra', '1212', '2222', 'marvin', 'pussy', 'charles', '7777777', 'winston', 'cocacola', '4444', 'shit', "junior"]

#checks if password is in list
if (password in passowords):
    print('found your password')
else:
    print(password + " password is not in list")
#made by Taco https://github.com/BigBoyTaco and BoomberBot https://github.com/BoomberBot