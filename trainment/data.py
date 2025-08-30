import random
import os
from typing import List
import pandas as pd

def get_productive_templates():
    """Retorna lista de templates para emails produtivos"""
    return [
        "Estou com {problema} no sistema {sistema}",
        "Preciso de suporte para {questao}",
        "Erro {codigo_erro} acontecendo",
        "Status do projeto {projeto}?",
        "Reunião sobre {assunto} às {hora}",
        "Prazo para {tarefa} é {data}",
        "O {sistema} apresentou falha crítica",
        "Solicito {recurso} para resolver {problema}",
        "Atualização necessária no {modulo}",
        "Bug reportado pelo cliente: {descricao}",
        "Configuração de {tecnologia} não está funcionando",
        "Necessário rollback da versão {versao}",
        "Problema de performance no {ambiente}",
        "Ticket #{numero} precisa ser priorizado",
        "Falha na integração com {servico_externo}",
        "Backup do {recurso} falhou",
        "Monitoramento detectou {anomalia}",
        "Acesso negado ao {recurso}",
    ]

def get_unproductive_templates():
    """Retorna lista de templates para emails não produtivos"""
    return [
        "{cumprimento}! Como você está?",
        "Parabéns pelo {evento}!",
        "{felicitacao} pela conquista!",
        "Desejo um ótimo {periodo}!",
        "Obrigado pela {ajuda}",
        "Que {sentimento} receber sua mensagem!",
        "Espero que esteja {estado}",
        "Tenha um {desejo}!",
        "Muito obrigado por {acao}!",
        "Fico feliz em {situacao}",
        "Desculpe pelo {incidente}",
        "Foi um prazer {experiencia}",
        "Agradeço pela {cortesia}",
        "Que bom saber que {novidade}!",
        "Desejo tudo de {qualidade} para você",
        "Até {momento}!",
        "Abraços e {votos}!",
        "Espero que {expectativa}",
        "Pensando em {pessoa_situacao}",
        "Lembranças de {evento_passado}",
    ]


problemas = ["erro", "falha", "bug", "problema crítico", "inconsistência", "timeout", "crash"]
sistemas = ["pagamento", "login", "database", "servidor", "API", "frontend", "backend", "mobile"]
questoes = ["permissão de acesso", "configuração", "instalação", "migração", "backup", "restore"]
codigos_erro = ["500", "404", "403", "502", "timeout", "connection_refused", "null_pointer"]
projetos = ["migração", "novo sistema", "atualização", "refatoração", "deploy", "release"]
assuntos = ["arquitetura", "performance", "segurança", "planejamento", "retrospectiva", "daily"]
horas = ["9h", "14h", "16h30", "10h", "15h"]
tarefas = ["implementação", "teste", "documentação", "review", "deploy", "homologação"]
datas = ["hoje", "amanhã", "sexta-feira", "próxima semana", "fim do sprint"]

cumprimentos = ["Bom dia", "Boa tarde", "Boa noite", "Olá", "Oi", "E aí"]
eventos = ["aniversário", "promoção", "casamento", "formatura", "novo emprego", "aposentadoria"]
felicitacoes = ["Parabéns", "Felicitações", "Meus parabéns", "Que alegria"]
periodos = ["final de semana", "feriado", "férias", "dia", "semana", "mês"]
ajudas = ["orientação", "ajuda", "suporte", "dica", "conselho", "apoio"]
sentimentos = ["alegria", "prazer", "felicidade", "satisfação", "honra"]
estados = ["bem", "ótimo", "com saúde", "feliz", "tranquilo", "descansado"]
desejos = ["excelente dia", "ótima semana", "bom final de semana", "boa sorte", "sucesso"]
acoes = ["pensar em mim", "lembrar", "ajudar", "apoiar", "orientar", "colaborar"]
situacoes = ["saber disso", "conhecê-lo", "trabalhar juntos", "poder ajudar"]
incidentes = ["atraso", "mal-entendido", "transtorno", "inconveniente", "demora"]
experiencias = ["conversar", "trabalhar juntos", "conhecê-lo", "colaborar", "participar"]
cortesias = ["gentileza", "atenção", "paciência", "compreensão", "educação"]
novidades = ["está tudo bem", "deu certo", "foi resolvido", "melhorou"]
qualidades = ["bom", "melhor", "ótimo", "maravilhoso", "excelente"]
momentos = ["mais tarde", "breve", "em breve", "logo", "na próxima"]
votos = ["bons votos", "muito carinho", "sucesso", "felicidade", "paz"]
expectativas = ["corra tudo bem", "seja um sucesso", "dê certo", "melhore logo"]
pessoas_situacoes = ["você", "sua família", "seus projetos", "seu trabalho", "sua saúde"]
eventos_passados = ["nossa conversa", "nosso projeto", "aquele dia", "a reunião", "o evento"]


# Função para gerar dataset sintético
def generate_dataset(num_samples_per_class:int=1000) -> List[dict]:
    """
    Gera dataset para treinamento
    
    Args:
        num_samples_per_class: Número de exemplos por classe (produtivo/não produtivo)
    
    Returns:
        List[dict]: Dataset com 'text' e 'label' (1=produtivo, 0=não produtivo)
    """
    dataset = []
    
    # Obter templates das funções
    productive_templates = get_productive_templates()
    unproductive_templates = get_unproductive_templates()
    
    # Gerar emails produtivos
    for _ in range(num_samples_per_class):
        template = random.choice(productive_templates)
        
        # Substituir placeholders
        filled_template = template.format(
            problema=random.choice(problemas),
            sistema=random.choice(sistemas),
            questao=random.choice(questoes),
            codigo_erro=random.choice(codigos_erro),
            projeto=random.choice(projetos),
            assunto=random.choice(assuntos),
            hora=random.choice(horas),
            tarefa=random.choice(tarefas),
            data=random.choice(datas),
            recurso=random.choice(sistemas + ["banco de dados", "servidor", "aplicação"]),
            modulo=random.choice(["autenticação", "pagamento", "relatórios", "dashboard"]),
            descricao=random.choice(problemas + ["lentidão", "travamento", "inconsistência"]),
            tecnologia=random.choice(["Docker", "Kubernetes", "PostgreSQL", "Redis", "Nginx"]),
            versao=random.choice(["v1.2.3", "v2.0.1", "latest", "stable"]),
            ambiente=random.choice(["produção", "homologação", "desenvolvimento", "staging"]),
            numero=random.choice(["12345", "67890", "11111", "22222"]),
            servico_externo=random.choice(["API de pagamento", "serviço de email", "CDN", "analytics"]),
            anomalia=random.choice(["alto uso de CPU", "memory leak", "conexões ociosas", "latência alta"])
        )
        
        dataset.append({
            "text": filled_template,
            "label": 1  # produtivo
        })
    
    # Gerar emails não produtivos
    for _ in range(num_samples_per_class):
        template = random.choice(unproductive_templates)
        
        # Substituir placeholders
        filled_template = template.format(
            cumprimento=random.choice(cumprimentos),
            evento=random.choice(eventos),
            felicitacao=random.choice(felicitacoes),
            periodo=random.choice(periodos),
            ajuda=random.choice(ajudas),
            sentimento=random.choice(sentimentos),
            estado=random.choice(estados),
            desejo=random.choice(desejos),
            acao=random.choice(acoes),
            situacao=random.choice(situacoes),
            incidente=random.choice(incidentes),
            experiencia=random.choice(experiencias),
            cortesia=random.choice(cortesias),
            novidade=random.choice(novidades),
            qualidade=random.choice(qualidades),
            momento=random.choice(momentos),
            votos=random.choice(votos),
            expectativa=random.choice(expectativas),
            pessoa_situacao=random.choice(pessoas_situacoes),
            evento_passado=random.choice(eventos_passados)
        )
        
        dataset.append({
            "text": filled_template,
            "label": 0  # não produtivo
        })
    
    # Embaralhar dataset
    random.shuffle(dataset)
    
    return dataset


def save_dataset_to_csv(
        dataset: List[dict], 
        filename:str="./app/assets/email_dataset.csv") -> None:
    """Salva dataset em CSV para usar no treinamento"""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    df = pd.DataFrame(dataset)
    df.to_csv(filename, index=False)


def generate_single_productive_email() -> str:
    """Gera um único email produtivo para teste"""
    template = random.choice(get_productive_templates())
    
    return template.format(
        problema=random.choice(problemas),
        sistema=random.choice(sistemas),
        questao=random.choice(questoes),
        codigo_erro=random.choice(codigos_erro),
        projeto=random.choice(projetos),
        assunto=random.choice(assuntos),
        hora=random.choice(horas),
        tarefa=random.choice(tarefas),
        data=random.choice(datas),
        recurso=random.choice(sistemas),
        modulo=random.choice(["autenticação", "pagamento", "relatórios"]),
        descricao=random.choice(problemas),
        tecnologia=random.choice(["Docker", "PostgreSQL", "Redis"]),
        versao=random.choice(["v1.2.3", "latest"]),
        ambiente=random.choice(["produção", "homologação"]),
        numero=random.choice(["12345", "67890"]),
        servico_externo=random.choice(["API de pagamento", "serviço de email"]),
        anomalia=random.choice(["alto uso de CPU", "memory leak"])
    )


def generate_single_unproductive_email() -> str:
    """Gera um único email não produtivo para teste"""
    template = random.choice(get_unproductive_templates())
    
    return template.format(
        cumprimento=random.choice(cumprimentos),
        evento=random.choice(eventos),
        felicitacao=random.choice(felicitacoes),
        periodo=random.choice(periodos),
        ajuda=random.choice(ajudas),
        sentimento=random.choice(sentimentos),
        estado=random.choice(estados),
        desejo=random.choice(desejos),
        acao=random.choice(acoes),
        situacao=random.choice(situacoes),
        incidente=random.choice(incidentes),
        experiencia=random.choice(experiencias),
        cortesia=random.choice(cortesias),
        novidade=random.choice(novidades),
        qualidade=random.choice(qualidades),
        momento=random.choice(momentos),
        votos=random.choice(votos),
        expectativa=random.choice(expectativas),
        pessoa_situacao=random.choice(pessoas_situacoes),
        evento_passado=random.choice(eventos_passados)
    )


# Exemplo de uso:
if __name__ == "__main__":   
    # Gerar dataset completo
    print("🔄 Gerando dataset completo...")
    dataset = generate_dataset(num_samples_per_class=1000)
    
    # Salvar em CSV
    save_dataset_to_csv(dataset)
    print(f"✅ Dataset salvo em email_dataset.csv")
    print(f"📊 Total de exemplos: {len(dataset)}")
    print(f"📈 Produtivos: {sum(1 for x in dataset if x['label'] == 1)}")
    print(f"📉 Não produtivos: {sum(1 for x in dataset if x['label'] == 0)}")




