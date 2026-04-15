import requests
import json

# Tu API key
API_KEY = "tu_clave"
BASE_URL = "https://api.api-ninjas.com/v1"

# Headers con autenticación
headers = {
    'X-Api-Key': API_KEY,
    'Content-Type': 'application/json'
}

class APINinjasCRUD:
    
    def get_quotes(self, category="inspirational", limit=1):
        """READ - Obtener citas famosas"""
        url = f"{BASE_URL}/quotes"
        params = {'category': category, 'limit': limit}
        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    def get_facts(self, animal="dog", limit=1):
        """READ - Obtener datos curiosos sobre animales"""
        url = f"{BASE_URL}/facts"
        params = {'animal': animal, 'limit': limit}
        
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    def get_age(self, name="John", country=None):
        """READ - Obtener estimación de edad por nombre"""
        url = f"{BASE_URL}/age"
        params = {'name': name}
        if country:
            params['country'] = country
            
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    def get_nutrition(self, query="apple"):
        """READ - Obtener información nutricional"""
        url = f"{BASE_URL}/nutrition"
        params = {'query': query}
        
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    def get_random_user(self):
        """READ - Obtener usuario aleatorio"""
        url = f"{BASE_URL}/randomuser"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"

# Ejemplo de uso
def main():
    api = APINinjasCRUD()
    
    print("=" * 50)
    print("1. GET Citas inspiracionales:")
    print("-" * 50)
    quotes = api.get_quotes(category="inspirational", limit=2)
    print(json.dumps(quotes, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 50)
    print("2. GET Datos curiosos de animales:")
    print("-" * 50)
    facts = api.get_facts(animal="dog", limit=2)
    print(json.dumps(facts, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 50)
    print("3. GET Estimación de edad:")
    print("-" * 50)
    age = api.get_age(name="Maria")
    print(json.dumps(age, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 50)
    print("4. GET Información nutricional:")
    print("-" * 50)
    nutrition = api.get_nutrition(query="banana")
    print(json.dumps(nutrition, indent=2, ensure_ascii=False))
    
    
    print("\n" + "=" * 50)
    print("5. GET Usuario aleatorio:")
    print("-" * 50)
    user = api.get_random_user()
    print(json.dumps(user, indent=2, ensure_ascii=False))
    
    # Nota sobre CRUD completo
    print("\n" + "=" * 50)
    print("NOTA SOBRE CRUD COMPLETO:")
    print("-" * 50)
    print("""La API Ninjas es principalmente de tipo READ (GET requests).
    Para un CRUD completo (POST, PUT, DELETE) normalmente necesitarías:
    
    - POST: api.post(url, headers=headers, json=data)
    - PUT: api.put(url, headers=headers, json=data)  
    - DELETE: api.delete(url, headers=headers)
    
    Ejemplo POST genérico:
    response = requests.post(f"{BASE_URL}/some-endpoint", 
                            headers=headers, 
                            json={"key": "value"})
    """)

if __name__ == "__main__":
    main()