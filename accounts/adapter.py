from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.lastname = form.cleaned_data.get('lastname')
        user.firstname = form.cleaned_data.get('firstname')
        user.age = form.cleaned_data.get('age')
        user.save()