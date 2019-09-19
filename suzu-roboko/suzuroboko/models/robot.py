from suzuroboko.models import ranking
from suzuroboko.views import console

DEFAULT_ROBOT_NAME='Suzu-roboko'

class Robot(object):
    def __init__(self,name=DEFAULT_ROBOT_NAME,user_name='',
                 speak_color='red'):
        self.name=name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        while True:
            template = console.get_template('hello.txt',self.speak_color)
            user_name=input(template.substitute({
                'robot_name':self.name}))
            if user_name:
                self.user_name=user_name
                break

class RestaurantRobot(Robot):

    def __init__(self,name=DEFAULT_ROBOT_NAME):
        super().__init__(name)
        self.ranking_model=ranking.RankingModel()

    def _hello_decorator(self):
        def wrapper(self):
            if not self.user_name:
                self.hello()
        return wrapper

    @_hello_decorator
    def recommend_restaurant(self):
        new_recommend_restaurant=self.ranking_model.get_most_popular()
        if not new_recommend_restaurant:
            return None

        will_recommend_restaurants=[new_recommend_restaurant]

        while True:
            template=console.get_template('greeting.txt',self.speak_color)
            is_yes=input(template.substitute({
                'robot_name':self.name,
                'user_name':self.user_name,
                'restaurant':new_recommend_restaurant}))
            if is_yes.lower()=='yes'or is_yes.lower()=='y':
              break

            if is_yes.lower()=='no' or is_yes.lower()=='n':
             new_recommend_restaurant=self.ranking_model.get_most_popular(
                not_list=will_recommend_restaurants)
            if not will_recommend_restaurants:
                break
            will_recommend_restaurants.append(new_recommend_restaurant)

    @_hello_decorator
    def ask_user_favorite(self):
        while True:
            template=console.get_template(
                'which_restaurant.txt',self.speak_color)
            restaurant=input(template.substitute({
                'robot_name':self.name,
                'user_name':self.user_name,
            }))

            if restaurant:
               self.ranking_model.increment(restaurant)
            break

    @_hello_decorator
    def thank_you(self):
        template=console.get_template('good_by.txt',self.speak_color)
        print(template.substitute({
            'robot_name':self.name,
            'user_name':self.user_name,
        }))











