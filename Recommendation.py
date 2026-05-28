user_pref={
    "Alice":["Ineption", "Titanic", "Avatar"],
    "Bob":["Inception", "Avatar", "Interstellar"],
    "Charlie":["Titanic", "The Notebook"]   
}

def recom_movies(user_name):
    user_movies=user_pref[user_name]

    recom=[]

    for other_user, movies in user_pref.items():
        if other_user != user_name:
            common_movies=set(user_movies) & set(movies)

            if len(common_movies) > 0:
                for movie in movies:
                    if movie not in user_movies:
                        recom.append(movie)

    return list(set(recom))

name= input("Enter your Name  : ")
if name in user_pref:
    print("Recommended Movies : ")
    print(recom_movies(name))
else:
    print("User not Found")