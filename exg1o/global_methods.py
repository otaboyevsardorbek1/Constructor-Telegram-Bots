from django.core.handlers.wsgi import WSGIRequest

def get_navbar_buttons_data(request: WSGIRequest):
	if request.user.is_authenticated:
		data = {
			'button_1': {
				'id': 'profileButtonLink',
				'onclick': f"window.location.href = '/account/view/{request.user.username}';",
				'text': 'Профиль'
			},
			'button_2': {
				'id': 'signOutButtonLink',
				'onclick': 'signOut();',
				'text': 'Выйти'
			},
			'button_3': {
				'id': 'konstruktorButtonLink',
				'onclick': f"window.location.href = '/account/konstruktor/{request.user.username}';",
				'text': 'Конструктор'
			}
		}
	else:
		data = {
			'button_1': {
				'id': 'authorizationButtonLink',
				'onclick': "window.location.href = '/authorization/';",
				'text': 'Авторизация'
			},
			'button_2': {
				'id': 'registrationButtonLink',
				'onclick': "window.location.href = '/registration/';",
				'text': 'Регистарция'
			},
			'button_3': {
				'id': 'hideKonstruktorButtonLink',
				'onclick': '',
				'text': ''
			}
		}
	return data