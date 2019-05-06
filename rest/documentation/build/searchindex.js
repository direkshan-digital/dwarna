Search.setIndex({docnames:["biobank","coauth","connection","index","server","setup","tests"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.todo":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["biobank.rst","coauth.rst","connection.rst","index.rst","server.rst","setup.rst","tests.rst"],objects:{"":{biobank:[0,0,0,"-"],coauth:[1,0,0,"-"],config:[4,0,0,"-"],connection:[2,0,0,"-"],main:[4,0,0,"-"],server:[4,0,0,"-"]},"biobank.handlers":{consent_handler:[0,0,0,"-"],exceptions:[0,0,0,"-"],handler:[0,0,0,"-"],participant_handler:[0,0,0,"-"],researcher_handler:[0,0,0,"-"],study_handler:[0,0,0,"-"]},"biobank.handlers.blockchain":{api:[0,0,0,"-"]},"biobank.handlers.blockchain.api":{BlockchainAPI:[0,1,1,""],hyperledger:[0,0,0,"-"]},"biobank.handlers.blockchain.api.BlockchainAPI":{create_participant:[0,2,1,""],create_study:[0,2,1,""],get_consent_trail:[0,2,1,""],get_studies_by_participant:[0,2,1,""],has_consent:[0,2,1,""],set_consent:[0,2,1,""]},"biobank.handlers.blockchain.api.hyperledger":{HyperledgerAPI:[0,1,1,""]},"biobank.handlers.blockchain.api.hyperledger.HyperledgerAPI":{__init__:[0,2,1,""],_card_exists:[0,2,1,""],_create_participant:[0,2,1,""],_get_participant_address:[0,2,1,""],_issue_identity:[0,2,1,""],_revoke_identity:[0,2,1,""],create_participant:[0,2,1,""],create_study:[0,2,1,""],get_card:[0,2,1,""],get_consent_trail:[0,2,1,""],get_studies_by_participant:[0,2,1,""],has_card:[0,2,1,""],has_consent:[0,2,1,""],save_cred_card:[0,2,1,""],set_consent:[0,2,1,""]},"biobank.handlers.consent_handler":{ConsentHandler:[0,1,1,""]},"biobank.handlers.consent_handler.ConsentHandler":{_set_attribute_value:[0,2,1,""],_set_consent:[0,2,1,""],get_attributes:[0,2,1,""],get_consent_trail:[0,2,1,""],get_participants_by_study:[0,2,1,""],get_studies_by_participant:[0,2,1,""],give_consent:[0,2,1,""],has_consent:[0,2,1,""],withdraw_consent:[0,2,1,""]},"biobank.handlers.exceptions":{general_exceptions:[0,0,0,"-"],study_exceptions:[0,0,0,"-"],user_exceptions:[0,0,0,"-"]},"biobank.handlers.exceptions.general_exceptions":{InputException:[0,3,1,""]},"biobank.handlers.exceptions.study_exceptions":{AttributeDoesNotExistException:[0,3,1,""],AttributeExistsException:[0,3,1,""],AttributeNotLinkedException:[0,3,1,""],InvalidStudyDurationException:[0,3,1,""],MissingAttributesException:[0,3,1,""],StudyDoesNotExistException:[0,3,1,""],StudyExistsException:[0,3,1,""],StudyExpiredException:[0,3,1,""]},"biobank.handlers.exceptions.user_exceptions":{BiobankerDoesNotExistException:[0,3,1,""],BiobankerExistsException:[0,3,1,""],ParticipantDoesNotExistException:[0,3,1,""],ParticipantExistsException:[0,3,1,""],ResearcherDoesNotExistException:[0,3,1,""],ResearcherExistsException:[0,3,1,""],UserExistsException:[0,3,1,""]},"biobank.handlers.handler":{PostgreSQLRouteHandler:[0,1,1,""],RouteHandler:[0,1,1,""],UserHandler:[0,1,1,""]},"biobank.handlers.handler.PostgreSQLRouteHandler":{_attribute_exists:[0,2,1,""],_attribute_id_exists:[0,2,1,""],_biobanker_exists:[0,2,1,""],_create_attribute:[0,2,1,""],_get_attribute_id:[0,2,1,""],_get_study_attributes:[0,2,1,""],_get_study_researchers:[0,2,1,""],_is_study_active:[0,2,1,""],_participant_exists:[0,2,1,""],_researcher_exists:[0,2,1,""],_sanitize:[0,2,1,""],_sanitize_dict:[0,2,1,""],_sanitize_list:[0,2,1,""],_study_exists:[0,2,1,""],_user_exists:[0,2,1,""],escape_escaped:[0,2,1,""],ping:[0,2,1,""],to_binary:[0,2,1,""]},"biobank.handlers.handler.RouteHandler":{_404_page_not_found:[0,2,1,""],__init__:[0,2,1,""],__weakref__:[0,4,1,""]},"biobank.handlers.participant_handler":{ParticipantHandler:[0,1,1,""]},"biobank.handlers.participant_handler.ParticipantHandler":{create_participant:[0,2,1,""],get_participants:[0,2,1,""],remove_participant_by_username:[0,2,1,""]},"biobank.handlers.researcher_handler":{ResearcherHandler:[0,1,1,""]},"biobank.handlers.researcher_handler.ResearcherHandler":{create_researcher:[0,2,1,""],get_researchers:[0,2,1,""],remove_researcher_by_username:[0,2,1,""]},"biobank.handlers.study_handler":{StudyHandler:[0,1,1,""]},"biobank.handlers.study_handler.StudyHandler":{_link_researchers:[0,2,1,""],_unlink_researchers:[0,2,1,""],create_study:[0,2,1,""],get_active_studies:[0,2,1,""],get_studies:[0,2,1,""],get_studies_by_researcher:[0,2,1,""],get_study_by_id:[0,2,1,""],remove_study:[0,2,1,""],update_study:[0,2,1,""]},"coauth.grants":{grants:[1,0,0,"-"]},"coauth.grants.grants":{CustomClientCredentialsGrant:[1,1,1,""],CustomClientCredentialsHandler:[1,1,1,""]},"coauth.grants.grants.CustomClientCredentialsGrant":{__call__:[1,2,1,""],__init__:[1,2,1,""]},"coauth.grants.grants.CustomClientCredentialsHandler":{__init__:[1,2,1,""],process:[1,2,1,""]},"coauth.oauth_request_handler":{OAuthRequestHandler:[1,1,1,""]},"coauth.oauth_request_handler.OAuthRequestHandler":{address_string:[1,2,1,""]},"coauth.token_store":{postgresql_token_store:[1,0,0,"-"]},"coauth.token_store.postgresql_token_store":{PostgresqlAccessTokenStore:[1,1,1,""],PostgresqlAuthCodeStore:[1,1,1,""],PostgresqlClientStore:[1,1,1,""]},"coauth.token_store.postgresql_token_store.PostgresqlAccessTokenStore":{__init__:[1,2,1,""],fetch_by_token:[1,2,1,""],save_token:[1,2,1,""]},"coauth.token_store.postgresql_token_store.PostgresqlClientStore":{__init__:[1,2,1,""],add_client:[1,2,1,""]},"connection.connection":{Connection:[2,1,1,""]},"connection.connection.Connection":{__weakref__:[2,4,1,""]},"connection.db_connection":{PostgreSQLConnection:[2,1,1,""]},"connection.db_connection.PostgreSQLConnection":{__init__:[2,2,1,""],__weakref__:[2,4,1,""],close:[2,2,1,""],commit:[2,2,1,""],copy:[2,2,1,""],count:[2,2,1,""],cursor:[2,2,1,""],execute:[2,2,1,""],exists:[2,2,1,""],reconnect:[2,2,1,""],select:[2,2,1,""],select_one:[2,2,1,""]},"server.application":{OAuthApplication:[4,1,1,""]},"server.application.OAuthApplication":{__call__:[4,2,1,""],__init__:[4,2,1,""],authorization_server:[4,4,1,""]},"server.authorization_server":{AuthorizationServer:[4,1,1,""]},"server.exceptions":{request_exceptions:[4,0,0,"-"]},"server.exceptions.request_exceptions":{InsufficientScopeException:[4,3,1,""],InvalidTokenException:[4,3,1,""],MethodNotAllowedException:[4,3,1,""],MissingArgumentException:[4,3,1,""],UnauthorizedDataAccessException:[4,3,1,""]},"server.exceptions.request_exceptions.InsufficientScopeException":{__init__:[4,2,1,""],__weakref__:[4,4,1,""]},"server.exceptions.request_exceptions.InvalidTokenException":{__init__:[4,2,1,""],__weakref__:[4,4,1,""]},"server.exceptions.request_exceptions.MethodNotAllowedException":{__init__:[4,2,1,""],__weakref__:[4,4,1,""]},"server.exceptions.request_exceptions.MissingArgumentException":{__init__:[4,2,1,""],__weakref__:[4,4,1,""]},"server.exceptions.request_exceptions.UnauthorizedDataAccessException":{__init__:[4,2,1,""],__weakref__:[4,4,1,""]},"server.resource_server":{ResourceServer:[4,1,1,""]},"server.resource_server.ResourceServer":{__init__:[4,2,1,""],_get_get_parameters:[4,2,1,""],_get_post_parameters:[4,2,1,""],_has_required_parameters:[4,2,1,""],_is_authorized:[4,2,1,""],_is_personal:[4,2,1,""],handle_request:[4,2,1,""]},"setup.minimal_schema":{create_schema:[5,6,1,""]},"setup.oauth_schema":{create_schema:[5,6,1,""]},"tests.environment":{CLIENT_ID:[6,5,1,""],CLIENT_SECRET:[6,5,1,""],PORT:[6,5,1,""],TEST_DATABASE:[6,5,1,""],TEST_OAUTH_DATABASE:[6,5,1,""],clear:[6,6,1,""],create_testing_environment:[6,6,1,""]},"tests.test":{BiobankTestCase:[6,1,1,""],retry:[6,6,1,""]},"tests.test.BiobankTestCase":{_get_access_token:[6,2,1,""],send_request:[6,2,1,""],send_volatile_request:[6,2,1,""],setUpClass:[6,7,1,""],tearDownClass:[6,7,1,""]},coauth:{oauth_request_handler:[1,0,0,"-"]},config:{biobanker_handler_class:[4,4,1,""],blockchain_admin_port:[4,5,1,""],blockchain_handler_class:[4,4,1,""],blockchain_host:[4,5,1,""],blockchain_multiuser_port:[4,5,1,""],consent_handler_class:[4,4,1,""],database:[4,5,1,""],default_scope:[4,5,1,""],generic_handler_class:[4,4,1,""],handler_classes:[4,5,1,""],handler_connector:[4,4,1,""],oauth_database:[4,5,1,""],participant_handler_class:[4,4,1,""],researcher_handler_class:[4,4,1,""],routes:[4,5,1,""],scopes:[4,5,1,""],study_handler_class:[4,4,1,""],token_expiry:[4,5,1,""]},connection:{connection:[2,0,0,"-"],db_connection:[2,0,0,"-"]},main:{main:[4,6,1,""],start_auth_server:[4,6,1,""]},server:{application:[4,0,0,"-"],authorization_server:[4,0,0,"-"],resource_server:[4,0,0,"-"]},setup:{minimal_schema:[5,0,0,"-"],oauth_schema:[5,0,0,"-"]},tests:{environment:[6,0,0,"-"],test:[6,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","exception","Python exception"],"4":["py","attribute","Python attribute"],"5":["py","data","Python data"],"6":["py","function","Python function"],"7":["py","classmethod","Python class method"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:exception","4":"py:attribute","5":"py:data","6":"py:function","7":"py:classmethod"},terms:{"boolean":[0,2,4],"byte":0,"case":[0,6],"class":[0,1,2,4,6],"default":[0,2,4,6],"export":0,"function":[0,1,2,4,5,6],"import":[0,4],"int":[0,1,2,4,6],"long":4,"new":[0,1,2,4],"return":[0,1,2,4,6],"short":0,"throw":2,"true":[0,1,4],"try":[4,6],For:[1,4],IDs:[0,1],Its:0,The:[0,1,2,4,6],Then:0,_404_page_not_found:0,__call__:[1,4],__init__:[0,1,2,4],__weakref__:[0,2,4],_attribute_exist:0,_attribute_id_exist:0,_biobanker_exist:0,_blockchain_connector:0,_card_exist:0,_connector:0,_create_attribut:0,_create_particip:0,_cursor_factori:2,_databas:2,_default_admin_port:0,_default_multiuser_port:0,_get_access_token:6,_get_attribute_id:0,_get_get_paramet:4,_get_participant_address:0,_get_post_paramet:4,_get_study_attribut:0,_get_study_research:0,_has_required_paramet:4,_host:[0,2],_is_author:4,_is_person:4,_is_study_act:0,_issue_ident:0,_link_research:0,_participant_exist:0,_password:2,_researcher_exist:0,_revoke_ident:0,_rout:4,_route_handl:4,_sanit:0,_sanitize_dict:0,_sanitize_list:0,_set_attribute_valu:0,_set_cons:0,_study_exist:0,_unlink_research:0,_user_exist:0,_usernam:2,abc:6,abl:0,about:0,accept:[0,4],access:[0,1,4,5,6],access_token:[0,1,4,6],access_token_id:1,access_token_stor:[1,4],accesstoken:[1,4],accesstokennotfound:1,accesstokenstor:[1,4],accur:4,act:[0,2],activ:0,active_onli:0,actual:[0,6],add:[1,4],add_client:1,added:[0,1],addit:[0,1],address:0,address_str:1,admin:[0,4,6],after:0,against:4,aid:0,alia:4,all:[0,2,4,6],allow:[0,1,4],along:6,alongsid:1,alreadi:0,also:[2,4],alter:6,alwai:0,ani:[0,2,4],anoth:[0,4],anyth:[0,2],api:[0,4],appli:0,applic:[1,2],arg:[0,1],argument:[0,4],aris:[0,6],arrai:[0,2],ask:1,associ:[0,2,4],assum:[0,1,5],attempt:4,attribut:[0,1,4],attribute_id:0,attributedoesnotexistexcept:0,attributeexistsexcept:0,attributenotlinkedexcept:0,auth_code_stor:4,auth_token_stor:4,authent:[0,1,4],authoiz:4,author:[0,1],authorization_serv:4,authorizationserv:4,authorize_uri:4,auto:1,avail:6,awri:2,back:[0,1,2],backend:[4,6],base:[0,1,2,4,5],batch:2,becaus:[0,1],been:[0,4],befor:[4,6],behalf:[1,2,6],behavior:1,being:[0,1,4],belong:[0,4],between:[0,1],binari:0,biobank:[4,5],biobank_oauth:4,biobank_oauth_test:6,biobank_test:6,biobanker_handl:4,biobanker_handler_class:4,biobankerdoesnotexistexcept:0,biobankerexistsexcept:0,biobankerhandl:4,biobanktestcas:6,blob:5,blockchain:[3,4,6],blockchain_admin_port:4,blockchain_connector:0,blockchain_handler_class:4,blockchain_host:4,blockchain_multiuser_port:4,blockchainapi:0,bodi:[0,4],bool:[0,1,2,4],both:0,build:4,built:4,busi:0,byte_str:0,call:[0,1,4],can:[0,2,4,5],cannot:[0,1],card:[0,4],case_sensit:0,caught:2,caus:4,chang:[0,2,6],change_card:4,charact:0,check:[0,2,4],classic:4,classmethod:6,clear:6,client:[1,4,6],client_address:1,client_authent:1,client_authentication_sourc:4,client_id:[1,6],client_secret:[1,6],client_stor:4,clientauthent:1,clientstor:4,close:2,coauth:1,code:[0,1,4,6],com:[4,5],command:2,commit:2,commun:0,compar:4,compon:4,compos:[0,4],config:4,configur:3,connect:[0,1,3,4,6],connector:0,consent_handl:[0,4],consent_handler_class:4,consenthandl:[0,4],consid:4,consol:1,constraint:0,construct:1,constructor:1,contain:[0,4],content:[0,3],convert:0,copi:2,correspond:6,count:2,creat:[0,1,2,4,5,6],create_biobank:4,create_particip:[0,4],create_research:[0,4],create_schema:5,create_studi:[0,4],create_testing_environ:6,creation:0,credenti:[0,1,2],current:0,cursor:2,cursor_factori:2,custom:[1,4],customclientcredentialsgr:1,customclientcredentialshandl:1,data:[0,1,3,4,6],databas:[0,1,4,5,6],datatyp:[1,4],date:0,db_connect:[2,4],dbapi:5,decor:6,default_admin_port:0,default_multiuser_port:0,default_scop:4,defin:[0,2,4],delet:4,deliv:4,descript:[0,4],desir:6,detail:0,dict:[0,1,2,4,6],dictcursorbas:2,dictionari:[0,4],differ:[0,2,4],differenti:0,doe:[0,2],duplic:2,durat:0,each:[0,4],effect:0,element:0,empti:0,enabl:1,encapsul:0,encod:4,end:[0,6],endpoint:[0,4,6],enough:4,ensur:[0,1,4],entri:1,env:4,env_var:4,environ:[0,1,3,4,5],equip:0,erron:4,error:[0,1,4],escap:0,escape_escap:0,establish:[2,4],even:1,exampl:4,except:[2,3],execut:[0,1,2],exist:[0,1,2,5],expect:[4,6],expir:4,expires_in:1,expiri:[1,4],extra:2,extract:[0,4],factori:2,fail:[0,2],fals:[0,2],fetch:[0,1,2,6],fetch_by_token:1,field:0,filter:0,first:[0,4],flow:4,follow:0,form:[0,4],format:1,found:0,from:[0,1,2,4,6],frontend:1,full:4,func:6,furthermor:1,gener:[1,2,4],general_except:0,generic_handler_class:4,get:[0,2,4,6],get_active_studi:[0,4],get_attribut:0,get_biobank:4,get_card:[0,4],get_consent_trail:[0,4],get_particip:[0,4],get_participants_by_studi:[0,4],get_research:[0,4],get_studi:[0,4],get_studies_by_particip:[0,4],get_studies_by_research:[0,4],get_study_by_id:[0,4],github:5,give:[0,1,4],give_cons:[0,4],given:[0,1,2,4,5],got:4,grant:[3,4],handl:[0,1,4],handle_request:4,handler:[3,4],handler_class:4,handler_connector:4,happen:0,has:[0,2,4],has_card:[0,4],has_cons:[0,4],have:0,header:4,held:6,help:4,his:0,homepag:[0,4],host:[0,2,4],hostnam:[0,2],how:[0,4],howev:0,http:[4,5,6],hyperledg:4,hyperledgerapi:[0,4],ident:0,identifi:[0,1],immedi:6,implement:[0,1,5],inact:0,includ:[0,4],inclus:0,incom:4,incorpor:0,incorrect:4,increment:1,index:3,indic:[0,2,4],individu:4,inform:[1,4],inherit:0,initi:[1,4],input:0,inputexcept:0,insert:0,instal:1,instanc:[1,2],instanti:0,instead:[0,1],insuffici:4,insufficientscopeexcept:4,interfac:[0,2],invalid:[0,1,4],invalidstudydurationexcept:0,invalidtokenexcept:4,invok:4,involv:1,issu:0,its:[0,1,4],itself:[1,2],job:0,json:0,just:[2,5],keep:6,kei:4,kind:0,know:1,known:[0,4],kwarg:[0,1],languag:1,last:6,lastrowid:1,later:0,leg:4,lifespan:1,link:[0,4],list:[0,2,4,6],listen:4,listen_port:4,live:4,localhost:4,log:1,longer:0,look:0,made:[0,1],mai:[0,2,4],main:4,make:6,manag:[3,4],match:0,meant:0,memori:[0,4],messag:[0,1,4],method:[4,6],methodnam:6,methodnotallowedexcept:4,mine:6,minimal_schema:5,mismatch:1,miss:4,missingargumentexcept:4,missingattributesexcept:0,mix:0,model:[0,6],modifi:1,modul:3,more:[1,4],moreov:[1,4],mozilla:4,multi:[0,4],must:0,mysql:[1,5],name:[0,1,2,4],need:[0,4,6],neg:0,never:6,none:[0,1,2,4,6],notic:0,number:[0,1,2,4,6],oauth2:[0,1,3,4],oauth:[3,4,6],oauth_connect:4,oauth_databas:4,oauth_request_handl:1,oauth_schema:5,oauthappl:4,oauthrequesthandl:1,object:[0,2,4],offer:0,one:[0,1,2,5,6],ones:[0,1],onli:[0,1,2,4],oper:0,option:4,origin:[1,4],other:0,otherwis:[2,4],out:[1,6],output:[0,6],over:[0,6],overriden:1,own:[0,4],owner:[1,4],page:[0,3],pagin:0,paramet:[0,1,2,4,6],pars:4,particip:4,participant_handl:[0,4],participant_handler_class:4,participantdoesnotexistexcept:0,participantexistsexcept:0,participanthandl:[0,4],pass:[0,4,6],password:2,path:4,perform:0,permiss:4,permit:4,person:4,ping:[0,4],port:[0,4,6],possibl:4,post:[4,6],postgersql:0,postgresql:[0,1,2,4],postgresql_token_stor:1,postgresqlaccesstokenstor:1,postgresqlauthcodestor:1,postgresqlclientstor:1,postgresqlconnect:[2,4],postgresqlroutehandl:[0,4],practic:1,process:[1,4],profil:0,protect:[4,6],provid:[0,4],psycopg2:2,purpos:0,put:4,python:[1,5],queri:[0,2,4],question:4,rais:[0,1,2,4],readi:0,realdictcursor:2,reason:1,receiv:[0,1,4,6],reconnect:2,refer:[0,2,4],refresh:5,reject:1,relat:0,remain:1,remov:[0,4],remove_biobank:4,remove_biobanker_by_usernam:4,remove_particip:4,remove_participant_by_usernam:[0,4],remove_research:4,remove_researcher_by_usernam:[0,4],remove_studi:[0,4],repli:0,repres:0,represent:0,request:[0,1,4,6],request_bodi:4,request_class:4,request_except:4,requir:[0,4,6],required_paramet:4,research:4,researcher_handl:[0,4],researcher_handler_class:4,researcherdoesnotexistexcept:0,researcherexistsexcept:0,researcherhandl:[0,4],resid:2,resourc:[1,6],resource_provid:4,resource_serv:4,resourceserv:4,respons:[0,1,4,6],response_class:4,rest:[0,4],restrict:4,result:[2,6],rethrown:2,retir:[0,4],retri:6,retriev:[0,1,6],revok:[0,4],roll:2,rout:[0,4],route_handl:4,routehandl:0,row:[1,2],run:0,runtest:6,same:[0,4],sampl:0,sanit:0,sanitize_escap:0,save:[0,2],save_cred_card:[0,4],save_token:1,schema:[1,3,6],scope:[1,4,6],scope_handl:1,search:[0,3],second:[1,4],secret:[1,6],secur:1,see:4,select:2,select_on:2,self:4,self_onli:4,send:[1,6],send_request:6,send_volatile_request:6,sensit:0,separ:0,server:[0,1,3,6],servic:[0,4],session:2,set:[0,4],set_cons:0,setup:[3,6],setupclass:6,share:4,should:[0,2,4,6],show:0,signatur:4,similar:1,sinc:[0,1],singl:[0,2],skeleton:0,some:[0,1,4,6],someth:2,sought:0,sourc:[0,1,2,4,5,6],special:0,specif:0,specifi:[0,1],split:4,standard:0,start:[0,1,4,6],start_auth_serv:4,start_respons:4,statement:2,statu:[0,4,6],status_cod:6,stop:6,storag:4,store:[0,3,4,5],str:[0,1,2,4,6],string:[0,1,4],strticip:0,studi:4,study_except:0,study_handl:[0,4],study_handler_class:4,study_id:[0,4],studyattributedoesnotexistexcept:0,studydoesnotexistexcept:0,studyexistsexcept:0,studyexpiredexcept:0,studyhandl:[0,4],succe:6,success:0,suppli:4,support:1,suppos:2,tabl:0,take:[0,1],taken:4,teardownclass:6,temp:[0,4],temporari:0,test:[3,4,5],test_databas:6,test_oauth_databas:6,thei:[0,4],theirs:4,them:[0,4],themselv:4,therefor:[0,1],thi:[0,1,2,4,5,6],those:0,though:1,three:[0,4],throughout:6,time:[0,1,4,6],timelin:0,timestamp:0,to_binari:0,token:[0,3,4,5,6],token_expiri:4,token_gener:[1,4],token_stor:1,token_uri:4,tokengener:[1,4],trail:0,transact:2,two:[0,1],type:[0,1,2,4,6],typic:0,unauthor:4,unauthorizeddataaccessexcept:4,unexpect:0,uniqu:[0,1,4],unlink:0,until:6,updat:[0,4],update_cons:4,update_studi:[0,4],upon:0,url:[0,4],use:[0,1,4,6],used:[0,1,2,4,5,6],useful:6,user:[1,4,6],user_except:0,user_id:[1,6],userexistsexcept:0,userhandl:0,usernam:[0,2,4],uses:[0,1],using:[0,1,2,4],usual:6,utf:4,valid:[0,1,4],valu:[0,6],variabl:[0,1,2,4],view_biobank:4,view_cons:4,view_particip:4,view_research:4,view_studi:4,volatil:6,wai:[1,4],weak:[0,2,4],web:[0,1,4],well:4,were:[1,2],whatsoev:4,when:[0,2,4,6],where:[0,2,4,6],whether:[0,2,4],which:[0,1,2,4,6],whom:1,whose:[0,6],with_cursor:2,withdraw:0,withdraw_cons:[0,4],wndhydrnt:5,workflow:0,would:1,wrap:6,wrapper:[0,2],write:0,wsgi:[1,4],www:4,xyz:6},titles:["Biobank Management","OAuth","Data Store Connections","Biobank Backend\u2019s Documentation","Server","Setup","Tests"],titleterms:{applic:4,author:4,backend:3,biobank:[0,3],blockchain:0,configur:4,connect:2,consent:0,data:2,databas:2,document:3,dynam:0,environ:6,except:[0,4],gener:0,grant:1,handler:[0,1],hyperledg:0,indic:3,manag:0,oauth2:5,oauth:1,particip:0,research:0,resourc:4,schema:5,server:4,setup:5,store:[1,2],studi:0,tabl:3,test:6,token:1,user:0}})