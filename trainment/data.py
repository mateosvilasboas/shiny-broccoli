import random
import os
from typing import List, Dict
import pandas as pd

# ============= VOCATIVOS =============
def get_vocativos():
    """Retorna lista de vocativos para emails"""
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Paulo", "Fernanda", "Ricardo", "Juliana"]
    cargos = ["Dr.", "Dra.", "Sr.", "Sra.", "Prof.", "Profa."]
    
    vocativos = []
    
    # Vocativos formais
    for nome in nomes:
        vocativos.extend([
            f"Prezado {nome}",
            f"Prezada {nome}",
            f"Caro {nome}",
            f"Cara {nome}",
            f"Estimado {nome}",
            f"Estimada {nome}",
        ])
    
    # Vocativos com cargo
    for cargo in cargos:
        for nome in nomes:
            vocativos.append(f"Prezado {cargo} {nome}")
    
    # Vocativos casuais
    for nome in nomes:
        vocativos.extend([
            f"Olá, {nome}",
            f"Oi {nome}",
            f"Bom dia, {nome}",
            f"Boa tarde, {nome}",
            f"E aí, {nome}",
        ])
    
    # Vocativos genéricos
    vocativos.extend([
        "Prezados",
        "Caros colegas",
        "Equipe",
        "Pessoal",
        "Olá pessoal",
        "Bom dia a todos",
        "Boa tarde, equipe",
    ])
    
    return vocativos

# ============= ASSINATURAS =============
def get_assinaturas():
    """Retorna lista de assinaturas para emails"""
    nomes = ["João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa", "Carlos Almeida", 
             "Lucia Ferreira", "Paulo Rodrigues", "Fernanda Lima", "Ricardo Souza", "Juliana Martins"]
    
    assinaturas = []
    
    # Assinaturas formais
    for nome in nomes:
        assinaturas.extend([
            f"Atenciosamente,\n{nome}",
            f"Cordialmente,\n{nome}",
            f"Respeitosamente,\n{nome}",
            f"Saudações,\n{nome}",
        ])
    
    # Assinaturas casuais
    for nome in nomes:
        assinaturas.extend([
            f"Abraços,\n{nome}",
            f"Um abraço,\n{nome}",
            f"Até mais,\n{nome}",
            f"Falou!\n{nome}",
            f"Grande abraço,\n{nome}",
        ])
    
    # Assinaturas com cargo
    cargos = ["Gerente de TI", "Analista de Sistemas", "Desenvolvedor", "Coordenador", 
              "Diretor", "Supervisor", "Especialista", "Consultor"]
    
    for nome in nomes[:5]:  # Apenas alguns nomes
        for cargo in cargos[:4]:  # Apenas alguns cargos
            assinaturas.append(f"Atenciosamente,\n{nome}\n{cargo}")
    
    return assinaturas

# ============= EMAILS PRODUTIVOS =============
def get_productive_email_templates():
    """Templates para emails produtivos completos"""
    return {
        # Solicitações urgentes
        "urgent_requests": [
            "Preciso de sua ajuda urgente com {problema} no {sistema}. O problema está afetando {impacto} e precisa ser resolvido até {prazo}.",
            "Situação crítica: {sistema} apresentou {problema}. Por favor, priorize esta demanda pois está impactando {impacto}.",
            "URGENTE: {problema} detectado em {ambiente}. Necessário intervenção imediata para evitar {consequencia}.",
            "Solicitação urgente de {recurso} para resolver {problema} que está afetando {impacto}.",
            "Preciso de autorização imediata para {acao} devido a {problema} em {sistema}.",
        ],
        
        # Consultas empresariais
        "business_queries": [
            "Gostaria de solicitar informações sobre {assunto} para {finalidade}. Preciso dos dados até {prazo}.",
            "Poderia me fornecer o status atual do {projeto}? Preciso atualizar {stakeholder}.",
            "Solicito esclarecimentos sobre {politica} para aplicar no {contexto}.",
            "Preciso de orientação sobre {procedimento} para {situacao}.",
            "Como devo proceder com {questao} considerando {restricao}?",
        ],
        
        # Reportes técnicos
        "technical_reports": [
            "Identificamos {problema} no {sistema} durante {periodo}. Impacto: {impacto}. Ação necessária: {acao}.",
            "Relatório de incidente: {evento} ocorrido em {data} causando {consequencia}. Status: {status}.",
            "Monitoramento detectou {anomalia} em {recurso}. Métricas: {metricas}. Requer investigação.",
            "Falha técnica reportada: {descricao}. Ambiente: {ambiente}. Severidade: {nivel}.",
            "Update técnico: {sistema} apresenta {comportamento}. Necessário {intervencao}.",
        ],
        
        # Pedidos de informação
        "info_requests": [
            "Solicito informações sobre {assunto} para {justificativa}. Prazo: {data}.",
            "Preciso dos seguintes dados: {dados} relacionados a {contexto}.",
            "Poderia me enviar {documento} referente a {assunto}?",
            "Solicitação de acesso a {recurso} para {finalidade}.",
            "Preciso de confirmação sobre {informacao} para {acao}.",
        ],
        
        # Propostas comerciais
        "commercial_proposals": [
            "Proposta comercial para {servico}: {descricao}. Valor: {valor}. Prazo: {prazo}.",
            "Orçamento solicitado para {projeto} incluindo {escopo}. Aguardo retorno.",
            "Apresento proposta de {solucao} para resolver {problema} com ROI de {beneficio}.",
            "Oferta especial de {produto} com {desconto}. Válida até {data}.",
            "Proposta de parceria para {objetivo} com benefícios mútuos.",
        ],
        
        # Escalações
        "escalations": [
            "Escalação necessária: {problema} não foi resolvido após {tempo}. Impacto: {consequencia}.",
            "Solicito intervenção da gerência para {situacao} que está bloqueando {atividade}.",
            "Escalando para nível superior: {issue} requer decisão executiva urgente.",
            "Problema recorrente {descricao} precisa de atenção da liderança.",
            "Escalação de conflito: {situacao} está impedindo {resultado}.",
        ],
    }

# ============= EMAILS NÃO PRODUTIVOS =============
def get_unproductive_email_templates():
    """Templates para emails não produtivos completos"""
    return {
        # Felicitações
        "congratulations": [
            "Parabéns pelo {conquista}! Sua dedicação e {qualidade} são inspiradoras.",
            "Ficamos muito felizes com seu {sucesso}! Merecido reconhecimento!",
            "Que alegria saber do seu {evento}! Desejamos muito {desejo}.",
            "Felicitações pela {realizacao}! É um exemplo para todos nós.",
            "Parabéns pelo {marco}! Sua {caracteristica} fez toda a diferença.",
        ],
        
        # Agradecimentos
        "gratitude": [
            "Muito obrigado pela {ajuda} com {situacao}. Sua {qualidade} foi fundamental.",
            "Agradeço imensamente por {acao}. Fez toda a diferença para {resultado}.",
            "Obrigado pela {cortesia} durante {evento}. Foi muito {sentimento}.",
            "Gostaria de expressar minha gratidão por {gesto}. Muito {adjetivo}!",
            "Agradeço pela {colaboracao} em {contexto}. Seu apoio foi {importancia}.",
        ],
        
        # Newsletters e comunicados
        "newsletters": [
            "Newsletter {mes}: Confira as {novidades} da empresa e {atualizacoes}.",
            "Comunicado {numero}: {informacao} será implementado a partir de {data}.",
            "Boletim informativo: {evento} acontecerá em {local} no dia {data}.",
            "Atualização mensal: {metricas} e {conquistas} da equipe.",
            "Informativo: Nova {politica} entra em vigor em {periodo}.",
        ],
        
        # Aniversários
        "birthdays": [
            "Feliz aniversário, {nome}! Desejamos um ano repleto de {desejos}!",
            "Parabéns pelos seus {idade} anos! Que seja um ano de {aspiracoes}!",
            "Hoje é dia de festa! Feliz aniversário e muito {sentimento}!",
            "Comemorando mais um ano de vida! Parabéns e {votos}!",
            "Aniversário especial merece {celebracao}! Felicidades!",
        ],
        
        # Conversas casuais
        "casual_chat": [
            "Como foram suas {periodo}? Espero que tenha {experiencia}!",
            "Lembrei de {memoria} e resolvi te contar sobre {assunto}.",
            "E aí, como está {situacao}? Tudo {estado} por aí?",
            "Que {sentimento} te encontrar! Como tem passado?",
            "Estava pensando em {topico} e lembrei de você.",
        ],
        
        # Anúncios corporativos
        "corporate_announcements": [
            "Temos o prazer de anunciar {novidade} que trará {beneficio} para todos.",
            "É com alegria que comunicamos {evento} que acontecerá em {data}.",
            "Anúncio importante: {mudanca} será implementada para {melhoria}.",
            "Compartilhamos com orgulho {conquista} da nossa equipe.",
            "Comunicamos {informacao} que entrará em vigor a partir de {periodo}.",
        ],
    }

# ============= DADOS PARA PREENCHIMENTO =============
def get_replacement_data():
    """Dados para substituir placeholders nos templates"""
    return {
        # Para emails produtivos
        "problemas": ["falha crítica", "erro 500", "timeout", "memory leak", "crash", "indisponibilidade", "lentidão", "bug crítico"],
        "sistemas": ["sistema de pagamento", "API principal", "banco de dados", "servidor de aplicação", "microserviço", "plataforma", "dashboard"],
        "ambientes": ["produção", "homologação", "staging", "desenvolvimento"],
        "impactos": ["todos os usuarios", "vendas online", "operacao critica", "SLA", "receita", "experiencia do cliente"],
        "prazos": ["hoje as 18h", "amanha cedo", "fim do dia", "proxima semana", "urgente"],
        "recursos": ["acesso admin", "servidor adicional", "licença", "aprovação", "orçamento", "equipe"],
        "consequencias": ["perda de receita", "insatisfação do cliente", "violação do SLA", "impacto na imagem", "multa contratual"],
        "acoes": ["restart do serviço", "rollback", "patch emergency", "escalação", "investigação", "monitoramento"],
        
        # Dados adicionais para emails produtivos
        "assuntos": ["relatório mensal", "política de segurança", "processo de deploy", "configuração de rede", "documentação técnica"],
        "finalidades": ["auditoria interna", "compliance", "relatório executivo", "análise de risco", "planejamento"],
        "projetos": ["migração cloud", "novo sistema", "atualização de segurança", "otimização de performance", "integração"],
        "stakeholders": ["a diretoria", "o cliente", "a equipe", "os investidores", "o departamento"],
        "politicas": ["política de backup", "normas de segurança", "procedimentos de deploy", "protocolo de incidentes"],
        "contextos": ["ambiente de produção", "novo projeto", "situação crítica", "processo atual", "implementação"],
        "procedimentos": ["recuperação de dados", "escalação de incidentes", "deploy de emergência", "backup manual"],
        "situacoes": ["falha do sistema", "manutenção programada", "incidente crítico", "atualização urgente"],
        "restricoes": ["política da empresa", "limitação orçamentária", "prazo apertado", "recursos limitados"],
        "questoes": ["aprovação de orçamento", "liberação de acesso", "validação técnica", "autorização de deploy"],
        
        # Para emails não produtivos  
        "conquistas": ["promoção", "certificação", "prêmio", "reconhecimento", "meta batida", "projeto concluído"],
        "sucessos": ["novo emprego", "formatura", "casamento", "nascimento", "aposentadoria", "conquista pessoal"],
        "qualidades": ["competência", "dedicação", "liderança", "criatividade", "persistência", "colaboração"],
        "desejos": ["felicidade", "sucesso", "realizações", "conquistas", "alegrias", "prosperidade"],
        "sentimentos": ["gratificante", "emocionante", "inspirador", "motivador", "especial", "marcante"],
        "cortesias": ["paciência", "gentileza", "atenção", "dedicação", "cuidado", "carinho"],
        "novidades": ["benefícios", "melhorias", "oportunidades", "eventos", "projetos", "iniciativas"],
        
        # Dados adicionais para emails não produtivos
        "eventos": ["aniversário da empresa", "festa de fim de ano", "workshop", "palestra", "confraternização"],
        "ajudas": ["orientação", "apoio", "suporte", "conselho", "dica", "colaboração"],
        "realizacoes": ["conclusão do projeto", "certificação obtida", "meta alcançada", "prêmio recebido"],
        "marcos": ["10 anos de empresa", "primeiro projeto", "milestone importante", "conquista pessoal"],
        "caracteristicas": ["dedicação", "profissionalismo", "competência", "liderança", "criatividade"],
        "gestos": ["ajuda prestada", "apoio dado", "colaboração", "orientação", "suporte oferecido"],
        "colaboracoes": ["trabalho em equipe", "projeto conjunto", "parceria", "suporte técnico"],
        "importancias": ["fundamental", "essencial", "muito importante", "decisivo", "crucial"],
        "datas": ["próxima semana", "15 de janeiro", "fim do mês", "início do próximo ano"],
        "locais": ["auditório principal", "sala de reuniões", "escritório central", "sede da empresa"],
        "documentos": ["relatório técnico", "manual de procedimentos", "especificação do projeto", "ata da reunião"],
        "dados": ["métricas de performance", "relatório de vendas", "análise de custos", "estatísticas de uso"],
        "justificativas": ["análise estratégica", "planejamento anual", "auditoria interna", "compliance regulatório"],
        
        # Dados adicionais para placeholders específicos
        "tempos": ["3 horas", "24 horas", "2 dias", "uma semana", "muito tempo"],
        "nomes": ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Paulo", "Fernanda"],
        "periodos": ["fim de semana", "feriado", "férias", "mês passado", "semana"],
        "informacoes": ["nova política", "procedimento atualizado", "mudança organizacional", "novo benefício"],
        "meses": ["janeiro", "fevereiro", "março", "abril", "maio", "junho"],
        "numeros": ["001/2024", "002/2024", "003/2024", "004/2024"],
        "atualizacoes": ["melhorias no sistema", "novos benefícios", "políticas atualizadas"],
        "metricas": ["100% de uptime", "95% de satisfação", "aumento de 20% na produtividade"],
        "idades": ["25", "30", "35", "40", "45", "50"],
        "aspiracoes": ["muito sucesso", "realizações pessoais", "conquistas profissionais"],
        "votos": ["muita felicidade", "muito sucesso", "paz e alegria", "realizações"],
        "celebracoes": ["uma festa especial", "um brinde", "comemorações", "momentos especiais"],
        "experiencias": ["se divertido", "aproveitado bem", "relaxado", "aprendido muito"],
        "memorias": ["nosso último projeto", "aquela reunião", "nossa conversa", "o evento passado"],
        "estados": ["bem", "ótimo", "tranquilo", "corrido", "interessante"],
        "topicos": ["inovação", "sustentabilidade", "tecnologia", "desenvolvimento"],
        "beneficios": ["maior eficiência", "melhor comunicação", "redução de custos"],
        "mudancas": ["nova estrutura organizacional", "processo otimizado", "ferramenta atualizada"],
        "melhorias": ["maior produtividade", "melhor qualidade", "experiência aprimorada"],
        
        # Dados técnicos adicionais
        "comportamentos": ["lentidão", "instabilidade", "falhas intermitentes", "timeout", "erro de conexão"],
        "intervencoes": ["restart", "investigação detalhada", "patch", "monitoramento", "escalação"],
        "resultados": ["melhoria significativa", "resolução completa", "otimização", "correção"],
        "adjetivos": ["impressionante", "útil", "valioso", "importante", "significativo"],
        "status": ["em andamento", "resolvido", "aguardando aprovação", "investigando"],
        "anomalias": ["picos de CPU", "memory leak", "conexões ativas altas", "latência elevada"],
        "descricoes": ["falha de conexão", "timeout de API", "erro de memória", "crash do serviço"],
        "niveis": ["crítico", "alto", "médio", "baixo"],
        "servicos": ["consultoria técnica", "suporte especializado", "desenvolvimento", "manutenção"],
        "valores": ["R$ 10000", "R$ 25000", "R$ 50000", "a combinar"],
        "escopos": ["análise completa", "implementação", "treinamento", "documentação"],
        "solucoes": ["migração para cloud", "otimização de performance", "automação", "monitoramento"],
        "produtos": ["licença premium", "serviço completo", "consultoria", "treinamento"],
        "descontos": ["20% de desconto", "condicoes especiais", "preco promocional"],
        "objetivos": ["crescimento mútuo", "inovação", "eficiência operacional", "redução de custos"],
        "atividades": ["desenvolvimento", "produção", "entrega", "planejamento"],
        "issues": ["problema crítico", "falha sistêmica", "bloqueio técnico", "conflito de recursos"],
    }

def generate_complete_email(template_type: str, is_productive: bool) -> str:
    """
    Gera um email completo com vocativo, corpo e assinatura
    
    Args:
        template_type: Tipo do template (urgent_requests, congratulations, etc.)
        is_productive: Se é email produtivo ou não
    
    Returns:
        str: Email completo formatado
    """
    vocativo = random.choice(get_vocativos())
    assinatura = random.choice(get_assinaturas())
    
    if is_productive:
        templates = get_productive_email_templates()
        corpo_template = random.choice(templates[template_type])
    else:
        templates = get_unproductive_email_templates()
        corpo_template = random.choice(templates[template_type])
    
    # Preencher placeholders
    replacement_data = get_replacement_data()
    corpo = corpo_template
    
    # Lista de todos os placeholders possíveis para substituir
    all_placeholders = {
        # Placeholders do dicionário principal
        "{problema}": "problemas",
        "{sistema}": "sistemas", 
        "{ambiente}": "ambientes",
        "{impacto}": "impactos",
        "{prazo}": "prazos",
        "{recurso}": "recursos",
        "{consequencia}": "consequencias",
        "{acao}": "acoes",
        "{assunto}": "assuntos",
        "{finalidade}": "finalidades",
        "{projeto}": "projetos",
        "{stakeholder}": "stakeholders",
        "{politica}": "politicas",
        "{contexto}": "contextos",
        "{procedimento}": "procedimentos",
        "{situacao}": "situacoes",
        "{restricao}": "restricoes",
        "{questao}": "questoes",
        "{conquista}": "conquistas",
        "{sucesso}": "sucessos",
        "{qualidade}": "qualidades",
        "{desejo}": "desejos",
        "{sentimento}": "sentimentos",
        "{cortesia}": "cortesias",
        "{novidade}": "novidades",
        "{evento}": "eventos",
        "{ajuda}": "ajudas",
        "{realizacao}": "realizacoes",
        "{marco}": "marcos",
        "{caracteristica}": "caracteristicas",
        "{gesto}": "gestos",
        "{colaboracao}": "colaboracoes",
        "{importancia}": "importancias",
        "{data}": "datas",
        "{local}": "locais",
        "{documento}": "documentos",
        "{dados}": "dados",
        "{justificativa}": "justificativas",
        "{tempo}": "tempos",
        "{nome}": "nomes",
        "{desejos}": "desejos",
        "{periodo}": "periodos",
        "{informacao}": "informacoes",
        "{mes}": "meses",
        "{numero}": "numeros",
        "{atualizacoes}": "atualizacoes",
        "{metricas}": "metricas",
        "{idade}": "idades",
        "{aspiracoes}": "aspiracoes",
        "{votos}": "votos",
        "{celebracao}": "celebracoes",
        "{experiencia}": "experiencias",
        "{memoria}": "memorias",
        "{estado}": "estados",
        "{topico}": "topicos",
        "{beneficio}": "beneficios",
        "{mudanca}": "mudancas",
        "{melhoria}": "melhorias",
        "{comportamento}": "comportamentos", 
        "{intervencao}": "intervencoes",
        "{resultado}": "resultados",
        "{adjetivo}": "adjetivos",
        "{status}": "status",
        "{anomalia}": "anomalias",
        "{descricao}": "descricoes",
        "{nivel}": "niveis",
        "{servico}": "servicos",
        "{valor}": "valores",
        "{escopo}": "escopos",
        "{solucao}": "solucoes",
        "{produto}": "produtos",
        "{desconto}": "descontos",
        "{objetivo}": "objetivos",
        "{atividade}": "atividades",
        "{issue}": "issues",
    }
    
    # Substituir todos os placeholders encontrados
    for placeholder, data_key in all_placeholders.items():
        if placeholder in corpo and data_key in replacement_data:
            corpo = corpo.replace(placeholder, random.choice(replacement_data[data_key]))
    
    # Montar email completo
    email_completo = f"{vocativo},\n\n{corpo}\n\n{assinatura}"
    
    return email_completo

def get_productive_templates():
    """Mantém compatibilidade com versão anterior - versão simplificada"""
    templates = get_productive_email_templates()
    simple_templates = []
    
    for category_templates in templates.values():
        simple_templates.extend(category_templates)
    
    return simple_templates

def get_unproductive_templates():
    """Mantém compatibilidade com versão anterior - versão simplificada"""
    templates = get_unproductive_email_templates()
    simple_templates = []
    
    for category_templates in templates.values():
        simple_templates.extend(category_templates)
    
    return simple_templates


def save_dataset_to_csv(
        dataset: List[dict], 
        filename: str = "./app/assets/email_dataset.csv") -> None:
    """Salva dataset em CSV para usar no treinamento"""
    
    # Criar diretório apenas se o filename tiver um diretório
    if os.path.dirname(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    df = pd.DataFrame(dataset)
    # Usar separador de ponto e vírgula para evitar problemas com vírgulas no texto
    df.to_csv(filename, index=False, sep=';', quoting=1)  # quoting=1 adiciona aspas quando necessário


def generate_single_productive_email() -> str:
    """Gera um único email produtivo completo para teste"""
    categories = ["urgent_requests", "business_queries", "technical_reports", 
                  "info_requests", "commercial_proposals", "escalations"]
    category = random.choice(categories)
    return generate_complete_email(category, is_productive=True)


def generate_single_unproductive_email() -> str:
    """Gera um único email não produtivo completo para teste"""
    categories = ["congratulations", "gratitude", "newsletters", 
                  "birthdays", "casual_chat", "corporate_announcements"]
    category = random.choice(categories)
    return generate_complete_email(category, is_productive=False)


def generate_dataset(num_samples_per_class: int = 1000) -> List[dict]:
    """
    Gera dataset para treinamento com emails completos
    
    Args:
        num_samples_per_class: Número de exemplos por classe (produtivo/não produtivo)
    
    Returns:
        List[dict]: Dataset com 'text' e 'label' (1=produtivo, 0=não produtivo)
    """
    dataset = []
    
    # Categorias de emails produtivos
    productive_categories = [
        "urgent_requests",
        "business_queries", 
        "technical_reports",
        "info_requests",
        "commercial_proposals",
        "escalations"
    ]
    
    # Categorias de emails não produtivos
    unproductive_categories = [
        "congratulations",
        "gratitude",
        "newsletters", 
        "birthdays",
        "casual_chat",
        "corporate_announcements"
    ]
    
    # Gerar emails produtivos
    emails_per_category = num_samples_per_class // len(productive_categories)
    remaining_emails = num_samples_per_class % len(productive_categories)
    
    for i, category in enumerate(productive_categories):
        # Distribuir emails restantes nas primeiras categorias
        num_emails = emails_per_category + (1 if i < remaining_emails else 0)
        
        for _ in range(num_emails):
            email_text = generate_complete_email(category, is_productive=True)
            dataset.append({
                "text": email_text,
                "label": 1  # produtivo
            })
    
    # Gerar emails não produtivos
    emails_per_category = num_samples_per_class // len(unproductive_categories)
    remaining_emails = num_samples_per_class % len(unproductive_categories)
    
    for i, category in enumerate(unproductive_categories):
        # Distribuir emails restantes nas primeiras categorias
        num_emails = emails_per_category + (1 if i < remaining_emails else 0)
        
        for _ in range(num_emails):
            email_text = generate_complete_email(category, is_productive=False)
            dataset.append({
                "text": email_text,
                "label": 0  # não produtivo
            })
    
    # Embaralhar dataset
    random.shuffle(dataset)
    
    return dataset


# Exemplo de uso:
if __name__ == "__main__":   
    # Testar geração de emails individuais
    print("📧 Exemplo de Email Produtivo:")
    print("=" * 50)
    print(generate_single_productive_email())
    print("\n" + "=" * 50)
    
    print("\n📧 Exemplo de Email Não Produtivo:")
    print("=" * 50)
    print(generate_single_unproductive_email())
    print("\n" + "=" * 50)
    
    # Gerar dataset completo
    print("\n🔄 Gerando dataset completo...")
    dataset = generate_dataset(num_samples_per_class=500)  # Menor para teste
    
    # Salvar em CSV
    save_dataset_to_csv(dataset)
    print(f"✅ Dataset salvo em email_dataset.csv")
    print(f"📊 Total de exemplos: {len(dataset)}")
    print(f"📈 Produtivos: {sum(1 for x in dataset if x['label'] == 1)}")
    print(f"📉 Não produtivos: {sum(1 for x in dataset if x['label'] == 0)}")
    
    # Mostrar alguns exemplos
    print(f"\n📝 Primeiros 3 emails do dataset:")
    for i, email in enumerate(dataset[:3]):
        label = "PRODUTIVO" if email['label'] == 1 else "NÃO PRODUTIVO"
        print(f"\n--- Email {i+1} ({label}) ---")
        print(email['text'][:200] + "..." if len(email['text']) > 200 else email['text'])




