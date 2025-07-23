--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 15.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

SET SESSION AUTHORIZATION DEFAULT;

ALTER TABLE public.auth_group DISABLE TRIGGER ALL;

COPY public.auth_group (id, name) FROM stdin;
\.


ALTER TABLE public.auth_group ENABLE TRIGGER ALL;

--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.django_content_type DISABLE TRIGGER ALL;

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	usuarios	usuario
7	usuarios	logusuario
8	empresas	empresa
9	empresas	setor
10	formulario	empresa
11	formulario	setor
12	respostas	resposta
13	formulario	pergunta
14	formulario	fator
15	formulario	acaorecomendada
16	empresas	pergunta
17	empresas	fator
18	empresas	acaorecomendada
19	painel	fator
20	painel	acao
21	painel	pergunta
22	painel	logacao
23	painel	setor
24	painel	empresa
\.


ALTER TABLE public.django_content_type ENABLE TRIGGER ALL;

--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_permission DISABLE TRIGGER ALL;

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add usuario	6	add_usuario
22	Can change usuario	6	change_usuario
23	Can delete usuario	6	delete_usuario
24	Can view usuario	6	view_usuario
25	Can add log usuario	7	add_logusuario
26	Can change log usuario	7	change_logusuario
27	Can delete log usuario	7	delete_logusuario
28	Can view log usuario	7	view_logusuario
29	Can add empresa	8	add_empresa
30	Can change empresa	8	change_empresa
31	Can delete empresa	8	delete_empresa
32	Can view empresa	8	view_empresa
33	Can add setor	9	add_setor
34	Can change setor	9	change_setor
35	Can delete setor	9	delete_setor
36	Can view setor	9	view_setor
37	Can add empresa	10	add_empresa
38	Can change empresa	10	change_empresa
39	Can delete empresa	10	delete_empresa
40	Can view empresa	10	view_empresa
41	Can add setor	11	add_setor
42	Can change setor	11	change_setor
43	Can delete setor	11	delete_setor
44	Can view setor	11	view_setor
45	Can add resposta	12	add_resposta
46	Can change resposta	12	change_resposta
47	Can delete resposta	12	delete_resposta
48	Can view resposta	12	view_resposta
49	Can add pergunta	13	add_pergunta
50	Can change pergunta	13	change_pergunta
51	Can delete pergunta	13	delete_pergunta
52	Can view pergunta	13	view_pergunta
53	Can add fator	14	add_fator
54	Can change fator	14	change_fator
55	Can delete fator	14	delete_fator
56	Can view fator	14	view_fator
57	Can add acao recomendada	15	add_acaorecomendada
58	Can change acao recomendada	15	change_acaorecomendada
59	Can delete acao recomendada	15	delete_acaorecomendada
60	Can view acao recomendada	15	view_acaorecomendada
61	Can add pergunta	16	add_pergunta
62	Can change pergunta	16	change_pergunta
63	Can delete pergunta	16	delete_pergunta
64	Can view pergunta	16	view_pergunta
65	Can add fator	17	add_fator
66	Can change fator	17	change_fator
67	Can delete fator	17	delete_fator
68	Can view fator	17	view_fator
69	Can add acao recomendada	18	add_acaorecomendada
70	Can change acao recomendada	18	change_acaorecomendada
71	Can delete acao recomendada	18	delete_acaorecomendada
72	Can view acao recomendada	18	view_acaorecomendada
73	Can add fator	19	add_fator
74	Can change fator	19	change_fator
75	Can delete fator	19	delete_fator
76	Can view fator	19	view_fator
77	Can add acao	20	add_acao
78	Can change acao	20	change_acao
79	Can delete acao	20	delete_acao
80	Can view acao	20	view_acao
81	Can add pergunta	21	add_pergunta
82	Can change pergunta	21	change_pergunta
83	Can delete pergunta	21	delete_pergunta
84	Can view pergunta	21	view_pergunta
85	Can add log acao	22	add_logacao
86	Can change log acao	22	change_logacao
87	Can delete log acao	22	delete_logacao
88	Can view log acao	22	view_logacao
89	Can add setor	23	add_setor
90	Can change setor	23	change_setor
91	Can delete setor	23	delete_setor
92	Can view setor	23	view_setor
93	Can add empresa	24	add_empresa
94	Can change empresa	24	change_empresa
95	Can delete empresa	24	delete_empresa
96	Can view empresa	24	view_empresa
\.


ALTER TABLE public.auth_permission ENABLE TRIGGER ALL;

--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group_permissions DISABLE TRIGGER ALL;

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


ALTER TABLE public.auth_group_permissions ENABLE TRIGGER ALL;

--
-- Data for Name: usuarios_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.usuarios_usuario DISABLE TRIGGER ALL;

COPY public.usuarios_usuario (id, password, last_login, is_superuser, email, nome_completo, cargo, is_active, is_staff) FROM stdin;
2	pbkdf2_sha256$1000000$V41MpIjlnfuVl7Av2mSSVz$oCEzmBMMfPiYSTpflrPK3RLBtcjOGqnS8ga6EmCkJcQ=	2025-07-22 12:44:51.085533-03	t	tulio.cliniseg@gmail.com	Tulio Adriano Aguiar	TST	t	t
1	pbkdf2_sha256$1000000$FzaXEWcEpf8uLX6t4I3W4E$08GztdQpCsa+C41JGtYzF6yBiKkuMbZ5W4kgwzqnX1A=	2025-07-22 12:57:37.465793-03	t	tulio.aguiar@hotmail.com	Tulio Aguiar	TST	t	t
\.


ALTER TABLE public.usuarios_usuario ENABLE TRIGGER ALL;

--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.django_admin_log DISABLE TRIGGER ALL;

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


ALTER TABLE public.django_admin_log ENABLE TRIGGER ALL;

--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.django_migrations DISABLE TRIGGER ALL;

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-07-14 16:15:39.903149-03
2	contenttypes	0002_remove_content_type_name	2025-07-14 16:15:39.903149-03
3	auth	0001_initial	2025-07-14 16:15:39.950015-03
4	auth	0002_alter_permission_name_max_length	2025-07-14 16:15:39.950015-03
5	auth	0003_alter_user_email_max_length	2025-07-14 16:15:39.950015-03
6	auth	0004_alter_user_username_opts	2025-07-14 16:15:39.950015-03
7	auth	0005_alter_user_last_login_null	2025-07-14 16:15:39.965647-03
8	auth	0006_require_contenttypes_0002	2025-07-14 16:15:39.965647-03
9	auth	0007_alter_validators_add_error_messages	2025-07-14 16:15:39.965647-03
10	auth	0008_alter_user_username_max_length	2025-07-14 16:15:39.965647-03
11	auth	0009_alter_user_last_name_max_length	2025-07-14 16:15:39.981256-03
12	auth	0010_alter_group_name_max_length	2025-07-14 16:15:39.981256-03
13	auth	0011_update_proxy_permissions	2025-07-14 16:15:39.981256-03
14	auth	0012_alter_user_first_name_max_length	2025-07-14 16:15:39.981256-03
15	usuarios	0001_initial	2025-07-14 16:15:40.048722-03
16	admin	0001_initial	2025-07-14 16:15:40.068688-03
17	admin	0002_logentry_remove_auto_add	2025-07-14 16:15:40.075717-03
18	admin	0003_logentry_add_action_flag_choices	2025-07-14 16:15:40.081594-03
19	empresas	0001_initial	2025-07-14 16:15:40.116591-03
20	formulario	0001_initial	2025-07-14 16:15:40.14083-03
21	respostas	0001_initial	2025-07-14 16:15:40.153615-03
22	respostas	0002_alter_resposta_setor	2025-07-14 16:15:40.168652-03
23	sessions	0001_initial	2025-07-14 16:15:40.182718-03
24	formulario	0002_fator_pergunta_acaorecomendada	2025-07-14 19:23:39.308857-03
25	empresas	0002_fator_pergunta_acaorecomendada	2025-07-14 20:15:35.154687-03
26	painel	0001_initial	2025-07-15 17:06:51.491032-03
27	painel	0002_logacao	2025-07-15 18:31:48.541576-03
28	painel	0003_acao_classificacao_fator_classificacao_risco_and_more	2025-07-15 20:24:48.160419-03
29	painel	0004_fator_ordem_alter_acao_classificacao_and_more	2025-07-15 21:57:42.148694-03
30	painel	0005_alter_fator_options_alter_fator_ordem	2025-07-15 22:01:34.765084-03
31	painel	0006_alter_pergunta_options_pergunta_numero	2025-07-16 16:25:00.384768-03
32	painel	0007_alter_pergunta_numero	2025-07-16 16:25:00.415981-03
33	painel	0008_alter_pergunta_numero	2025-07-16 16:25:00.415981-03
34	painel	0009_alter_pergunta_numero	2025-07-16 16:25:00.431588-03
35	painel	0010_alter_pergunta_numero	2025-07-16 16:25:00.431588-03
36	painel	0011_alter_pergunta_numero	2025-07-16 16:25:00.447234-03
37	painel	0012_empresa_setor	2025-07-18 14:31:21.242027-03
38	empresas	0002_remove_setor_funcionarios_setor_num_funcionarios	2025-07-18 14:52:06.777227-03
39	empresas	0003_alter_empresa_options_alter_setor_options_and_more	2025-07-21 19:16:01.305716-03
40	formulario	0002_alter_empresa_options_alter_setor_options_and_more	2025-07-21 20:57:57.182662-03
\.


ALTER TABLE public.django_migrations ENABLE TRIGGER ALL;

--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.django_session DISABLE TRIGGER ALL;

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
tgwmyjfipvffypz28w2ckq11eps9t7os	.eJxVjMsOwiAQRf-FtSFMoTxcuvcbyNAZpGogKe3K-O_apAvd3nPOfYmI21ri1nmJM4mzAHH63RJOD647oDvWW5NTq-syJ7kr8qBdXhvx83K4fwcFe_nWZtQeOSuvDXhMga13wSM4hjxAGIiJAFXyYw7aWqddQqU0GaXAZY3i_QHP1zdA:1ubnrE:WTIWSkUXqTftDAnHoKImPZhlJ_cqX4HwGwt7rzprcnE	2025-07-29 19:10:40.779985-03
lwq800uxkr3acen73m0see1j1bjxw396	.eJxVjE0OgjAYBe_StWlsKa24dM8ZyPfzsKiBhMLKeHfThIVu38y8txlo3_KwF6zDpOZqvDn9bkzyxFyBPmi-L1aWeVsntlWxBy22XxSv2-H-HWQqudZgQFnaFJSDsCQZY-eaGGIHRB8CANGGkBK5i7ZjQjwnEteJ9w2bzxcwzzld:1ue0fZ:cXrBlvlTpXfOiJ8YY-VFq3bLA-69QyNzZFn3JD90CME	2025-08-04 21:15:45.325378-03
r56ohwd8sm27jjvsaxqdjtwi8021xnmm	.eJxVjMsOwiAQRf-FtSFMoTxcuvcbyNAZpGogKe3K-O_apAvd3nPOfYmI21ri1nmJM4mzAHH63RJOD647oDvWW5NTq-syJ7kr8qBdXhvx83K4fwcFe_nWZtQeOSuvDXhMga13wSM4hjxAGIiJAFXyYw7aWqddQqU0GaXAZY3i_QHP1zdA:1ueBQG:9unG6nS9fA4jJq_oyARZA_hu7x10UO5VavsCZRptzZs	2025-08-05 08:44:40.386803-03
n9xg10cznqz158qzngp0y5nmpuzodwbt	.eJxVjE0OgjAYBe_StWlsKa24dM8ZyPfzsKiBhMLKeHfThIVu38y8txlo3_KwF6zDpOZqvDn9bkzyxFyBPmi-L1aWeVsntlWxBy22XxSv2-H-HWQqudZgQFnaFJSDsCQZY-eaGGIHRB8CANGGkBK5i7ZjQjwnEteJ9w2bzxcwzzld:1ueFAh:FO-ogiIIFx02tgRuRynO_8otZ2OlBFeSxI77qYaESBg	2025-08-05 12:44:51.101062-03
4rw27xjq6ytvw8cydj42jviob7tcht49	.eJxVjMsOwiAQRf-FtSFMoTxcuvcbyNAZpGogKe3K-O_apAvd3nPOfYmI21ri1nmJM4mzAHH63RJOD647oDvWW5NTq-syJ7kr8qBdXhvx83K4fwcFe_nWZtQeOSuvDXhMga13wSM4hjxAGIiJAFXyYw7aWqddQqU0GaXAZY3i_QHP1zdA:1ueFN3:2il9m4gxrEb4TcdaGOCEgg4IJnKIel48EJPy0ce-Eb0	2025-08-05 12:57:37.467187-03
\.


ALTER TABLE public.django_session ENABLE TRIGGER ALL;

--
-- Data for Name: empresas_fator; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.empresas_fator DISABLE TRIGGER ALL;

COPY public.empresas_fator (id, numero, nome) FROM stdin;
\.


ALTER TABLE public.empresas_fator ENABLE TRIGGER ALL;

--
-- Data for Name: empresas_acaorecomendada; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.empresas_acaorecomendada DISABLE TRIGGER ALL;

COPY public.empresas_acaorecomendada (id, risco, texto, fator_id) FROM stdin;
\.


ALTER TABLE public.empresas_acaorecomendada ENABLE TRIGGER ALL;

--
-- Data for Name: empresas_empresa; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.empresas_empresa DISABLE TRIGGER ALL;

COPY public.empresas_empresa (id, nome, cnpj, slug) FROM stdin;
12	CLINISEG Medicina e Segurança do Trabalho	54.066.572/0001-00	cliniseg
\.


ALTER TABLE public.empresas_empresa ENABLE TRIGGER ALL;

--
-- Data for Name: empresas_pergunta; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.empresas_pergunta DISABLE TRIGGER ALL;

COPY public.empresas_pergunta (id, texto, fator_id) FROM stdin;
\.


ALTER TABLE public.empresas_pergunta ENABLE TRIGGER ALL;

--
-- Data for Name: empresas_setor; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.empresas_setor DISABLE TRIGGER ALL;

COPY public.empresas_setor (id, nome_setor, empresa_id, num_funcionarios) FROM stdin;
48	ENFERMAGEM	12	1
49	FONOAUDIOLOGIA	12	1
50	SEGURANÇA DO TRABALHO	12	3
51	ADMINISTRATIVO	12	3
\.


ALTER TABLE public.empresas_setor ENABLE TRIGGER ALL;

--
-- Data for Name: formulario_fator; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.formulario_fator DISABLE TRIGGER ALL;

COPY public.formulario_fator (id, numero, nome) FROM stdin;
\.


ALTER TABLE public.formulario_fator ENABLE TRIGGER ALL;

--
-- Data for Name: formulario_acaorecomendada; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.formulario_acaorecomendada DISABLE TRIGGER ALL;

COPY public.formulario_acaorecomendada (id, risco, texto, fator_id) FROM stdin;
\.


ALTER TABLE public.formulario_acaorecomendada ENABLE TRIGGER ALL;

--
-- Data for Name: formulario_empresa; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.formulario_empresa DISABLE TRIGGER ALL;

COPY public.formulario_empresa (id, nome, cnpj, slug) FROM stdin;
\.


ALTER TABLE public.formulario_empresa ENABLE TRIGGER ALL;

--
-- Data for Name: formulario_pergunta; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.formulario_pergunta DISABLE TRIGGER ALL;

COPY public.formulario_pergunta (id, texto, fator_id) FROM stdin;
\.


ALTER TABLE public.formulario_pergunta ENABLE TRIGGER ALL;

--
-- Data for Name: formulario_setor; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.formulario_setor DISABLE TRIGGER ALL;

COPY public.formulario_setor (id, empresa_id, nome_setor, num_funcionarios) FROM stdin;
\.


ALTER TABLE public.formulario_setor ENABLE TRIGGER ALL;

--
-- Data for Name: painel_fator; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_fator DISABLE TRIGGER ALL;

COPY public.painel_fator (id, nome, descricao, classificacao_risco, ordem) FROM stdin;
21	Variação de turnos		Baixo	3
24	Trabalho remunerado por produção		Baixo	6
23	Metas rigorosas		Baixo	5
34	Multitarefas com alta carga cognitiva		Baixo	16
19	Trabalho sem pausas para descanso		Baixo	1
20	Ritmo intenso de trabalho		Baixo	2
22	Capacidade insuficiente para as tarefas		Baixo	4
28	Exigência cognitiva elevada		Baixo	10
36	Falta de autonomia		Baixo	18
31	Demandas emocionais/afetivas		Baixo	13
32	Assédio no trabalho		Baixo	14
33	Demandas divergentes		Baixo	15
35	Insatisfação no trabalho		Baixo	17
25	Desequilíbrio trabalho x descanso		Baixo	7
27	Sobrecarga mental		Baixo	9
30	Conflitos no trabalho		Baixo	12
26	Situações de estresse		Moderado	8
29	Comunicação deficiente		Baixo	11
\.


ALTER TABLE public.painel_fator ENABLE TRIGGER ALL;

--
-- Data for Name: painel_acao; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_acao DISABLE TRIGGER ALL;

COPY public.painel_acao (id, descricao, fator_id, classificacao) FROM stdin;
76	Manter e reforçar as boas práticas de gestão de pausas e descansos.	19	Baixo
77	Avaliar a otimização das pausas e a comunicação sobre sua importância.	19	Moderado
78	Revisar a frequência e duração das pausas, garantindo sua efetividade na recuperação.	19	Elevado
79	Intervenção urgente para garantir o direito a pausas adequadas e o respeito aos limites de jornada.	19	Crítico
80	Manter um ritmo de trabalho que favoreça o bem-estar e a qualidade das entregas.	20	Baixo
81	Monitorar o ritmo de trabalho e a percepção de tempo para tarefas, buscando otimizações.	20	Moderado
83	Reavaliar urgentemente o ritmo de trabalho e as expectativas de produtividade, com foco na saúde do trabalhador.	20	Crítico
84	Manter a organização de turnos e horários que se harmonizam com o bem-estar.	21	Baixo
85	Investigar pontos de ajuste na organização de turnos para melhor harmonia com a vida do trabalhador.	21	Moderado
86	Revisar a política de variação de turnos, considerando seu impacto no bem-estar e ritmo biológico.	21	Elevado
87	Intervenção imediata na gestão de turnos para mitigar impactos severos na saúde e bem-estar.	21	Crítico
88	Manter e aprimorar os programas de treinamento e capacitação contínuos.	22	Baixo
89	Avaliar a pertinência e suficiência dos treinamentos para novas demandas ou tecnologias.	22	Moderado
90	Reforçar os programas de capacitação e fornecer mais suporte para o desenvolvimento de habilidades.	22	Elevado
91	Revisar urgentemente a matriz de treinamento e o processo de integração, garantindo a qualificação para as tarefas.	22	Crítico
92	Manter a definição de metas realistas, que consideram recursos e habilidades dos colaboradores.	23	Baixo
93	Realizar acompanhamento individual das metas e condições de trabalho, ajustando quando necessário.	23	Moderado
94	Revisar o processo de definição de metas, garantindo que sejam alcançáveis e seguras, com recursos adequados.	23	Elevado
95	Intervenção imediata na política de metas, considerando redefinição e avaliação dos impactos na saúde.	23	Crítico
96	Manter a estrutura de remuneração que motive e traga conforto aos colaboradores.	24	Baixo
97	Monitorar a percepção sobre a remuneração por produção, buscando entender eventuais desconfortos.	24	Moderado
98	Avaliar o sistema de remuneração por produção, considerando seus impactos no bem-estar e na pressão.	24	Elevado
99	Análise e redefinição urgentes do sistema de remuneração por produção, se estiver gerando pressão excessiva.	24	Crítico
100	Promover a cultura de equilíbrio entre vida profissional e pessoal, incentivando o descanso.	25	Baixo
101	Oferecer recursos e flexibilidade para que os colaboradores gerenciem seu tempo e energia.	25	Moderado
102	Revisar as práticas de gestão de jornada e demandas, buscando maior equilíbrio entre trabalho e vida pessoal.	25	Elevado
103	Intervenção imediata para garantir o direito ao tempo de descanso e à vida pessoal, com apoio à desconexão.	25	Crítico
104	Manter um ambiente de trabalho que promova o equilíbrio emocional e a tranquilidade.	26	Baixo
105	Identificar e gerenciar fontes de estresse potenciais, oferecendo suporte proativo.	26	Moderado
106	Analisar e reestruturar as demandas de trabalho para reduzir o estresse, focando na qualidade de vida.	26	Elevado
107	Intervenção urgente para mitigar fatores de estresse, com apoio psicológico e reavaliação de processos.	26	Crítico
108	Manter o volume de responsabilidades e a cultura de aprendizado com erros.	27	Baixo
109	Monitorar o volume de trabalho e incentivar a busca por apoio em momentos de pressão.	27	Moderado
110	Revisar a distribuição de tarefas e responsabilidades, garantindo tempo para aprendizado e recuperação.	27	Elevado
111	Intervenção imediata na gestão da carga de trabalho e na cultura de erros, buscando equilíbrio e segurança psicológica.	27	Crítico
112	Manter a exigência cognitiva em níveis saudáveis, sem sobrecarga.	28	Baixo
113	Avaliar a intensidade da concentração e atenção exigidas, oferecendo estratégias de manejo.	28	Moderado
114	Ajustar as demandas cognitivas e oferecer pausas ativas para evitar a sobrecarga mental.	28	Elevado
115	Reavaliar urgentemente as tarefas que exigem alta carga cognitiva, buscando formas de otimização e revezamento.	28	Crítico
116	Manter um ambiente que favoreça a comunicação clara e a interação social.	29	Baixo
117	Melhorar canais e ferramentas de comunicação, e estimular momentos de troca social.	29	Moderado
118	Analisar as barreiras à comunicação e interação no ambiente físico, buscando soluções ergonômicas e organizacionais.	29	Elevado
119	Intervenção urgente para remover obstáculos à comunicação eficaz e promover a interação social positiva.	29	Crítico
120	Manter um ambiente de trabalho colaborativo e livre de conflitos interpessoais.	30	Baixo
121	Promover workshops de comunicação e resolução de conflitos para fortalecer as relações.	30	Moderado
122	Implementar políticas claras de gestão de conflitos e mediação, incentivando a resolução saudável.	30	Elevado
123	Intervenção imediata para endereçar conflitos e restaurar um ambiente de colaboração e respeito mútuo.	30	Crítico
124	Manter um ambiente onde a expressão autêntica de sentimentos é possível e equilibrada com as exigências.	31	Baixo
125	Oferecer suporte e ferramentas para o manejo das emoções no ambiente de trabalho.	31	Moderado
126	Avaliar as exigências emocionais da função e seus impactos, buscando formas de proteção e apoio.	31	Elevado
82	Analisar cargas de trabalho e prazos, ajustando-os para evitar sobrecarga e perda de qualidade.	20	Elevado
127	Intervenção urgente para proteger o bem-estar emocional dos colaboradores, redefinindo expectativas ou oferecendo apoio especializado.	31	Crítico
128	Manter um ambiente de trabalho respeitoso, seguro e livre de assédio e punições excessivas.	32	Baixo
129	Reforçar a cultura de respeito, os canais de denúncia e as políticas de não assédio.	32	Moderado
130	Implementar ou fortalecer políticas antiassédio, treinamento de lideranças e canais de denúncia confidenciais.	32	Elevado
131	Intervenção imediata e rigorosa para combater assédio, punições indevidas e criar um ambiente de segurança psicológica.	32	Crítico
132	Manter a clareza e consistência nas informações, metas e feedback sobre o desempenho.	33	Baixo
133	Otimizar os processos de comunicação de metas e o sistema de feedback para maior clareza.	33	Moderado
134	Revisar os processos de comunicação interna e alinhamento de expectativas, garantindo clareza e consistência.	33	Elevado
135	Reestruturar urgentemente os canais de comunicação e as políticas de feedback para eliminar inconsistências.	33	Crítico
136	Manter a capacidade de gerenciar múltiplas tarefas sem prejuízo ao bem-estar e desempenho.	34	Baixo
137	Oferecer treinamento em gestão de tempo e prioridades para otimizar o multitarefa.	34	Moderado
138	Analisar a necessidade de multitarefas, buscando reduzir a carga cognitiva excessiva e seus impactos.	34	Elevado
139	Intervenção imediata na organização das tarefas e processos para reduzir a sobrecarga cognitiva e proteger o bem-estar.	34	Crítico
140	Manter e fortalecer o reconhecimento, a valorização e a motivação no trabalho.	35	Baixo
141	Desenvolver programas de reconhecimento e valorização, além de oportunidades de crescimento.	35	Moderado
142	Avaliar os fatores que causam insatisfação, como reconhecimento, valorização e oportunidades de desenvolvimento.	35	Elevado
143	Intervenção imediata para reverter a insatisfação, investindo em reconhecimento, desenvolvimento e engajamento.	35	Crítico
144	Manter uma cultura que incentive a autonomia e a participação dos colaboradores.	36	Baixo
145	Promover a delegação de responsabilidades e o desenvolvimento de habilidades de liderança.	36	Moderado
146	Revisar os níveis de autonomia e a participação dos colaboradores, buscando maior empoderamento.	36	Elevado
147	Intervenção urgente para aumentar a autonomia dos colaboradores e promover a participação ativa na tomada de decisões.	36	Crítico
\.


ALTER TABLE public.painel_acao ENABLE TRIGGER ALL;

--
-- Data for Name: painel_empresa; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_empresa DISABLE TRIGGER ALL;

COPY public.painel_empresa (id, nome, cnpj, slug) FROM stdin;
\.


ALTER TABLE public.painel_empresa ENABLE TRIGGER ALL;

--
-- Data for Name: painel_logacao; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_logacao DISABLE TRIGGER ALL;

COPY public.painel_logacao (id, acao, data_hora, executado_por_id, usuario_alvo_id) FROM stdin;
\.


ALTER TABLE public.painel_logacao ENABLE TRIGGER ALL;

--
-- Data for Name: painel_pergunta; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_pergunta DISABLE TRIGGER ALL;

COPY public.painel_pergunta (id, texto, fator_id, numero) FROM stdin;
74	As pausas oferecidas (conforme CLT) são adequadas para a minha recuperação física e mental.	19	2
75	O ritmo do meu trabalho me permite manter o bem estar e atenção durante toda a jornada.	20	3
76	Tenho tempo suficiente para realizar minhas tarefas com a qualidade que eu considero ideal.	20	4
78	Recebo instruções e treinamentos adequados para me sentir seguro e preparado para as minhas atividades.	22	6
79	As capacitações que recebo são adequadas e suficientes para realizar meu trabalho com segurança e qualidade.	22	7
80	Consigo atingir as metas de produtividade com os recursos disponíveis e de forma segura.	23	8
81	As metas de trabalho são realistas e consideram minhas habilidades e capacidade para realizá-las.	23	9
82	A forma como meu salário é definido pela minha produção me traz motivação e conforto.	24	10
83	Consigo equilibrar meu tempo de trabalho com o tempo necessário para meu descanso.	25	11
84	Meu trabalho me permite ter tempo e energia para a vida pessoal e familiar.	25	12
85	Meu trabalho contribui positivamente para meu equilíbrio emocional e bem-estar no dia a dia.	26	13
86	As demandas do meu trabalho são organizadas de forma que consigo manter minha tranquilidade e qualidade de sono.	26	14
87	A quantidade de tarefas que exigem minha atenção e raciocínio são adequadas.	27	15
88	O volume das minhas responsabilidades no trabalho me permite manter meu equilíbrio emocional e me sentir energizado(a).	27	16
89	Tenho liberdade para errar e aprender com meus enganos, mesmo quando a pressão no trabalho é grande.	27	17
90	Consigo manter o nível de concentração e atenção que meu trabalho exige, sem me sobrecarregar.	28	18
91	As condições do meu ambiente de trabalho (como ruído, isolamento, distância física ou regras rígidas) facilitam a comunicação necessária para realizar minhas tarefas de forma eficaz.	29	19
92	Meu ambiente físico de trabalho facilita a troca de ideias e a interação social com meus colegas.	29	20
93	Percebo que o ambiente de trabalho é tranquilo e livre de conflitos interpessoais.	30	21
94	Sinto que há uma boa colaboração e apoio entre os colegas no meu ambiente de trabalho.	30	22
95	Consigo expressar meus sentimentos de forma autêntica enquanto atendo às exigências da minha função.	31	23
96	As exigências emocionais do trabalho apoiam meu equilíbrio mental, físico e social.	31	24
97	Sinto que o ambiente de trabalho é respeitoso e livre de assédio.	32	25
98	Me sinto seguro(a) para lidar com erros e aprender com eles, sem medo de punições excessivas.	32	26
99	As informações e metas que recebo para a execução do meu trabalho são claras e consistentes, facilitando meu desempenho.	33	27
100	Recebo feedback claro sobre o meu desempenho, que me ajuda a entender como estou “indo” no trabalho.	33	28
101	Consigo gerenciar múltiplas tarefas ao mesmo tempo, mantendo o foco e um bom nível de energia mental.	34	29
102	As tarefas que eu realizo ao mesmo tempo no trabalho favorecem meu bem-estar, contribuindo para meu conforto físico e mental e um bom desempenho.	34	30
103	Estou satisfeito(a) e realizado(a) com as atividades que desempenho no meu trabalho atual.	35	31
104	Meu trabalho e minhas contribuições são reconhecidos e valorizados pela organização.	35	32
105	Sinto-me motivado(a) e engajado(a) para continuar realizando meu trabalho.	35	33
106	Sinto que há espaço para sugerir melhorias e que minhas ideias são consideradas pela empresa.	36	34
107	Meus superiores estão abertos a ouvir minhas preocupações e sugestões no trabalho.	36	35
77	A variação de turnos (manhã, tarde, noite) se harmoniza com meu bem-estar e o ritmo do meu trabalho.	21	5
73	O meu tempo de descanso é suficiente para manter a disposição e a atenção no trabalho.	19	1
\.


ALTER TABLE public.painel_pergunta ENABLE TRIGGER ALL;

--
-- Data for Name: painel_setor; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.painel_setor DISABLE TRIGGER ALL;

COPY public.painel_setor (id, nome_setor, num_funcionarios, empresa_id) FROM stdin;
\.


ALTER TABLE public.painel_setor ENABLE TRIGGER ALL;

--
-- Data for Name: respostas_resposta; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.respostas_resposta DISABLE TRIGGER ALL;

COPY public.respostas_resposta (id, setor_id, sexo, faixa_etaria, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, data_envio, empresa_id) FROM stdin;
67	51	Feminino	26 a 35 anos	3	5	2	2	2	2	2	2	2	5	5	5	5	5	1	4	5	2	5	1	1	2	2	2	2	5	2	2	5	5	4	4	4	1	3	2025-07-22 13:17:53.025932-03	12
\.


ALTER TABLE public.respostas_resposta ENABLE TRIGGER ALL;

--
-- Data for Name: usuarios_logusuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.usuarios_logusuario DISABLE TRIGGER ALL;

COPY public.usuarios_logusuario (id, acao, data_hora, executado_por_id, usuario_alvo_id) FROM stdin;
\.


ALTER TABLE public.usuarios_logusuario ENABLE TRIGGER ALL;

--
-- Data for Name: usuarios_usuario_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.usuarios_usuario_groups DISABLE TRIGGER ALL;

COPY public.usuarios_usuario_groups (id, usuario_id, group_id) FROM stdin;
\.


ALTER TABLE public.usuarios_usuario_groups ENABLE TRIGGER ALL;

--
-- Data for Name: usuarios_usuario_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

ALTER TABLE public.usuarios_usuario_user_permissions DISABLE TRIGGER ALL;

COPY public.usuarios_usuario_user_permissions (id, usuario_id, permission_id) FROM stdin;
\.


ALTER TABLE public.usuarios_usuario_user_permissions ENABLE TRIGGER ALL;

--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 96, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 24, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 40, true);


--
-- Name: empresas_acaorecomendada_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.empresas_acaorecomendada_id_seq', 1, false);


--
-- Name: empresas_empresa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.empresas_empresa_id_seq', 12, true);


--
-- Name: empresas_fator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.empresas_fator_id_seq', 1, false);


--
-- Name: empresas_pergunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.empresas_pergunta_id_seq', 1, false);


--
-- Name: empresas_setor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.empresas_setor_id_seq', 51, true);


--
-- Name: formulario_acaorecomendada_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formulario_acaorecomendada_id_seq', 1, false);


--
-- Name: formulario_empresa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formulario_empresa_id_seq', 1, false);


--
-- Name: formulario_fator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formulario_fator_id_seq', 1, false);


--
-- Name: formulario_pergunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formulario_pergunta_id_seq', 1, false);


--
-- Name: formulario_setor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.formulario_setor_id_seq', 1, false);


--
-- Name: painel_acao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_acao_id_seq', 147, true);


--
-- Name: painel_empresa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_empresa_id_seq', 1, false);


--
-- Name: painel_fator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_fator_id_seq', 36, true);


--
-- Name: painel_logacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_logacao_id_seq', 1, false);


--
-- Name: painel_pergunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_pergunta_id_seq', 107, true);


--
-- Name: painel_setor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.painel_setor_id_seq', 1, false);


--
-- Name: respostas_resposta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.respostas_resposta_id_seq', 67, true);


--
-- Name: usuarios_logusuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_logusuario_id_seq', 1, false);


--
-- Name: usuarios_usuario_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_usuario_groups_id_seq', 1, false);


--
-- Name: usuarios_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_usuario_id_seq', 2, true);


--
-- Name: usuarios_usuario_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_usuario_user_permissions_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

