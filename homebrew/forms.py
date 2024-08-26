from django import forms
from .models import Homebrew, Item, Weapon, Armor, Career


INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl border'


class NewHomebrewForm(forms.ModelForm):
    class Meta:
        abstract = True
        model = Homebrew
        fields = ('name', 'image', 'description')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': INPUT_CLASSES})
            }


class NewItemForm(NewHomebrewForm):
    class Meta(NewHomebrewForm.Meta):
        model = Item
        fields = NewHomebrewForm.Meta.fields+ ('value', 'coinage')

        widgets = NewHomebrewForm.Meta.widgets
        widgets['value'] = forms.TextInput(attrs=
        {
            'placeholder': 'Value',
            'class' : INPUT_CLASSES,
        })
        widgets['coinage'] = forms.Select(attrs={'class': INPUT_CLASSES})


class NewWeaponForm(NewItemForm):
    class Meta(NewItemForm.Meta):
        model = Weapon
        fields = NewItemForm.Meta.fields + ('primary_stat', 'multiplayer', 'modifier')

        widgets = NewItemForm.Meta.widgets
        widgets['primary_stat'] = forms.Select(attrs={'class' : INPUT_CLASSES})
        widgets['multiplayer'] = forms.TextInput(attrs=
        {
            'placeholder': 'Multiplayer',
            'class' : INPUT_CLASSES
        })
        widgets['modifier'] = forms.TextInput(attrs=
        {
            'placeholder': 'Modifier',
            'class' : INPUT_CLASSES
        })


class NewArmorForm(NewItemForm):
    class Meta(NewItemForm.Meta):
        model = Armor
        fields = NewItemForm.Meta.fields + ('armor_points', 'location_covered')

        widgets = NewItemForm.Meta.widgets
        widgets['armor_points'] = forms.TextInput(attrs=
        {
            'placeholder': 'Armor Points',
            'class' : INPUT_CLASSES
        })
        widgets['location_covered'] = forms.Select(attrs={'class' : INPUT_CLASSES})


class NewCareerForm(NewHomebrewForm):
    class Meta(NewHomebrewForm.Meta):
        model = Career
        fields = NewHomebrewForm.Meta.fields + ('weapon_skill', 'balistic_skill', 'strength', 'toughness', 'agility',
                                                'intelligence', 'will_power', 'fellowship', 'attacks', 'wounds',
                                                'strength_bonus', 'toughness_bonus', 'movement', 'magic',
                                                'insanity_points', 'fate_points', 'skills', 'talents', 'trappings',
                                                'career_entries', 'career_exits')

        widgets = NewHomebrewForm.Meta.widgets
        # main profile
        widgets['weapon_skill'] = forms.TextInput(attrs=
        {
            'placeholder': 'WS',
            'class': INPUT_CLASSES
        })
        widgets['balistic_skill'] = forms.TextInput(attrs=
        {
            'placeholder': 'BS',
            'class': INPUT_CLASSES
        })
        widgets['strength'] = forms.TextInput(attrs=
        {
            'placeholder': 'S',
            'class': INPUT_CLASSES
        })
        widgets['toughness'] = forms.TextInput(attrs=
        {
            'placeholder': 'T',
            'class': INPUT_CLASSES
        })
        widgets['agility'] = forms.TextInput(attrs=
        {
            'placeholder': 'Ag',
            'class': INPUT_CLASSES
        })
        widgets['intelligence'] = forms.TextInput(attrs=
        {
            'placeholder': 'Int',
            'class': INPUT_CLASSES
        })
        widgets['will_power'] = forms.TextInput(attrs=
        {
            'placeholder': 'WP',
            'class': INPUT_CLASSES
        })
        widgets['fellowship'] = forms.TextInput(attrs=
        {
            'placeholder': 'Fel',
            'class': INPUT_CLASSES
        })
        # secondary profile
        widgets['attacks'] = forms.TextInput(attrs=
        {
            'placeholder': 'A',
            'class': INPUT_CLASSES
        })
        widgets['wounds'] = forms.TextInput(attrs=
        {
            'placeholder': 'W',
            'class': INPUT_CLASSES
        })
        widgets['strength_bonus'] = forms.TextInput(attrs=
        {
            'placeholder': 'SB',
            'class': INPUT_CLASSES
        })
        widgets['toughness_bonus'] = forms.TextInput(attrs=
        {
            'placeholder': 'TB',
            'class': INPUT_CLASSES
        })
        widgets['movement'] = forms.TextInput(attrs=
        {
            'placeholder': 'M',
            'class': INPUT_CLASSES
        })
        widgets['magic'] = forms.TextInput(attrs=
        {
            'placeholder': 'Mag',
            'class': INPUT_CLASSES
        })
        widgets['insanity_points'] = forms.TextInput(attrs=
        {
            'placeholder': 'IP',
            'class': INPUT_CLASSES
        })
        widgets['fate_points'] = forms.TextInput(attrs=
        {
            'placeholder': 'FP',
            'class': INPUT_CLASSES
        })
        # rest
        widgets['skills'] = forms.TextInput(attrs=
        {
            'placeholder': 'Skills',
            'class': INPUT_CLASSES
         })
        widgets['talents'] = forms.TextInput(attrs=
         {
             'placeholder': 'Talents',
             'class': INPUT_CLASSES
         })
        widgets['trappings'] = forms.TextInput(attrs=
        {
           'placeholder': 'Trappings',
           'class': INPUT_CLASSES
        })
        widgets['career_entries'] = forms.TextInput(attrs=
        {
            'placeholder': 'Career Entries',
            'class': INPUT_CLASSES
        })
        widgets['career_exits'] = forms.TextInput(attrs=
        {
          'placeholder': 'Career Exits',
          'class': INPUT_CLASSES
        })
