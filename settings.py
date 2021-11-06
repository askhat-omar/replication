from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 5.00,
    'doc': "",
}

SESSION_CONFIGS = [
    dict(
        name='DynPortBlue',
        display_name="Changing Probabilities Portfolio First",
        num_demo_participants=1,
        app_sequence=['introduction',
                      'dynamic_portfolio_instructions',
                      'dynamic_portfolio_chp',
                      'dynamic_iterative_chp',
                      'dynamic_portfolio_results',
                      'static_portfolio_chp',
                      'crt',
                      'survey',
                      'finalpage'],
        round1_T=3,
        round2_T=4,
        color='blue'
    ),
    dict(
        name='DynPortRed',
        display_name="Changing Probs Iterative First",
        num_demo_participants=1,
        app_sequence=['introduction',
                      'dynamic_portfolio_instructions',
                      'dynamic_iterative_chp',
                      'dynamic_portfolio_chp',
                      'dynamic_portfolio_results',
                      'static_portfolio_chp',
                      'crt',
                      'survey',
                      'finalpage'],
        round1_T=3,
        round2_T=4,
        color='red'
    ),
    dict(
        name='DynPortGreen',
        display_name="IID Portfolio First",
        num_demo_participants=1,
        app_sequence=['introduction',
                      'dynamic_portfolio_instructions',
                      'dynamic_portfolio',
                      'dynamic_iterative',
                      'dynamic_portfolio_results',
                      'static_portfolio',
                      'crt',
                      'survey',
                      'finalpage'],
        round1_T=3,
        round2_T=4,
        color='green'
    ),
    dict(
        name='DynPortYellow',
        display_name="IID Iterative First",
        num_demo_participants=1,
        app_sequence=['introduction',
                      'dynamic_portfolio_instructions',
                      'dynamic_iterative',
                      'dynamic_portfolio',
                      'dynamic_portfolio_results',
                      'static_portfolio',
                      'crt',
                      'survey',
                      'finalpage'],
        round1_T=3,
        round2_T=4,
        color='yellow'
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AUD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '@p7=^gv5pzv0udwk!c0b0hboi#0z5t0-#8v&!*y=zj4km!t@-^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
