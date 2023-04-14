#template to obtain the App information
template={
    'swagger':'2.0',
    'info':{
    'title':'Online food delivery system',
    'description':'an online food delivery for Group one- witi-cohort 2 APIs',
    'contact':{
    'responsibleOrganisation':'Group One Witi-Cohort 2',
    'responsibleDeveloper':'Shellah, Doreen and Flavia',
    'email':'shellahemmanuella@gmail.com',

    },
    'version':'1.0'
    },

    'basePath':'api/v1', #base bash for blueprint registration
    'schemes':['http','https'], #for security of apis

    'securityDefinitions':{
    'Bearer':{ #bearer type of authentication
    'type':'apiKey',
    'name':'Authorization',
    'in':'header',
    'description':'JWT Authorization header using the bearer scheme'
    }
    },


}

swagger_config={
    'headers':[],
    'specs':[{
    'endpoint':'apispec',
    'route':'/apispec.json', #defines the json version of the document
    'rule)filter': lambda rule: True,
    'model_filter': lambda tag: True
    }],
    'static_url_path':'/flasgger_static', #generate the css to show on the documentation
    'swagger_ui': True, #helps to visualise things in the best way
    'specs_route':'/' #default route on the home page

}