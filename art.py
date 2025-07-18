logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""










whyYouShouldHireMe = {}
hired = False

while not hired:
    whyYouShouldHireMe["reasonOne"] = \
        "Strong work ethic and always strive for excellence."
    whyYouShouldHireMe["reasonTwo"] = \
        "Quick learner and can adapt to new environments."
    whyYouShouldHireMe["reasonThree"] = \
        "Positive attitude and work well in collaborative teams."

    print("Reasons why you should hire me:")
    for key, value in whyYouShouldHireMe.items():
        print(f"{key}: {value}")