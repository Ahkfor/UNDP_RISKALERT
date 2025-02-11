from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class HAPIRecommender:
    
    HAPI_columns = [
        'Humanitarian Need',
        'Refugee',
        'Returnee',
        'Operational Presence',
        'Funding',
        'Conflict Event',
        'National Risk',
        'Food Price',
        'Food Security',
        'Population',
        'Poverty Rate'
    ]
    
    
    def __init__(self, summary):
        self.summary = summary
        self.correlation_scores = []
        self.compute_correlations()
    
    def compute_correlations(self):
        # Load pre-trained Sentence-BERT model
        sbert_model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast and accurate

        def compute_sbert_similarity(word, article):
            embeddings = sbert_model.encode([word, article])  # Get embeddings
            return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]  # Compute similarity
        
        # Compute correlation scoresvvvvvvvvvvvvnnmcB
        for column in self.HAPI_columns:
            correlation_score = compute_sbert_similarity(column, self.summary)
            self.correlation_scores.append(correlation_score)
        
        self.correlation_scores = sorted(zip(self.HAPI_columns, self.correlation_scores), key=lambda x: x[1], reverse=True)

summary = "The article outlines the complex emergency situation in Ukraine, including the surge in conflict-related civilian casualties, as recorded by the Office of the UN High Commissioner for Human Rights (OHCHR) from 1st to 31st March 2020. This was the highest monthly figure since September 2019. The situation in Ukraine is further exacerbated by the global impact of the COVID-19 pandemic, which has forced over 10 million people to flee their homes in search of safety, with 6.5 million internally displaced. The UN Human Rights Monitoring Mission in Ukraine has been monitoring the situation and has recorded over 10,000 civilian casualties since the beginning of the Russian Federation's armed attack on 24th February 2022. The article also highlights the discrimination faced by people of African descent at Ukraine's borders, and the need for protection for those with disabilities and older people who are caught up in the violence. Additionally, the response to the emergency situation must be grounded in principles of public trust, transparency, respect, and empathy for the most vulnerable. The global impact of the conflict in Ukraine is significant, as Russia and Ukraine account for a significant amount of the world's wheat supply, which is set to cause a sharp rise in global grain prices. Moreover, Save the Children estimates that at least 40% of people fleeing the conflict are children, putting them at risk of hunger, illness, trafficking, and abuse.The article ends by emphasizing the need for a comprehensive response to the emergency situation in Ukraine and the world, including the COVID-19 pandemic, that prioritizes the protection and support of vulnerable populations."

a = HAPIRecommender(summary)
print(a.correlation_scores)