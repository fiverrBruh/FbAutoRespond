from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        user = client.fetchUserInfo(author_id)[author_id]
        print(user.name)
        # this is your text... just change it the way you want.
        mytext = "Hello "+ str(user.name) + ".... Thank you so much for your interest. \
        The Property Mgmt Company is in the process of accepting applications. To get started, there is a three step process \
        \n1) Complete the eligibility form (https://goo.gl/sp9Wzh),\
        \n 2) Complete Registration (with your email address - We will send you the link), \
        and lastly\n  3) Complete the application.\n\n Please call if you have question " + str(user.name) + \
          " . \nThank You!\n Douglas Group Realty | Keller Williams Central."
        message_object.text = mytext
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)
# enter your email and password below. (Donot remove the inverted commas)
# eg. client = EchoBot("shivamgohel@gmail.com", "12345")
username = input("enter your email:")
password = input("enter your password:")
client = EchoBot(username, password)
client.listen()


