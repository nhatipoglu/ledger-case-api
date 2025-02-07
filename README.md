# Ledger Case Study API

## FastAPI + PostgreSQL + Docker

Bu proje, **FastAPI**, **PostgreSQL**, **Alembic** ve **Docker** kullanılarak geliştirilmiş bir **Ledger (Hesap Yönetimi) API** uygulamasıdır. API, kullanıcıların bakiyelerini yönetmelerini ve işlem yapmalarını sağlar.

---

## **Özellikler**
- **FastAPI** ile yüksek performanslı API geliştirme
- **PostgreSQL** ile veri yönetimi
- **Alembic** ile veritabanı migration yönetimi
- **Docker Compose** ile kolay kurulum ve dağıtım
- **Swagger UI** (`/docs`) ve **Redoc UI** (`/redoc`) destekli API dokümantasyonu

---

## **Kurulum ve Çalıştırma**

### **1. Bağımlılıkları Yükleme**
Eğer **Docker kullanmadan** projeyi çalıştırmak istiyorsanız, aşağıdaki komut ile bağımlılıkları yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

### **2. Çevresel Değişkenleri Yapılandırma**
Proje dizininde bir **`.env`** dosyası oluşturun ve veritabanı bağlantı bilgilerini girin:

```ini
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/yourdatabase
```

---

## **PostgreSQL ve FastAPI'yi Docker ile Çalıştırma**
Bu proje, **Docker Compose** kullanılarak PostgreSQL ve FastAPI'yi kolayca çalıştıracak şekilde yapılandırılmıştır.

Aşağıdaki komutları sırasıyla çalıştırarak **Docker ortamını başlatabilirsiniz**:

```bash
docker-compose up --build
```

Eğer konteynerleri **arka planda** çalıştırmak isterseniz:

```bash
docker-compose up -d
```

Tüm servisleri durdurmak için:

```bash
docker-compose down
```

Başarılı bir şekilde çalıştırıldığında aşağıdaki adreslerden erişim sağlanabilir:

- **FastAPI API:** [http://localhost:5200/api/ledger](http://localhost:5200/api/ledger)
- **Swagger UI:** [http://localhost:5200/api/swagger](http://localhost:5200/api/swagger)
- **Redoc UI:** [http://localhost:5200/api/redoc](http://localhost:5200/api/redoc)

---

## **Veritabanı Migration Yönetimi (Alembic)**

**Alembic**, veritabanı değişikliklerini yönetmek için kullanılan bir migration aracıdır.

Aşağıdaki komutları kullanarak **migration işlemlerini gerçekleştirebilirsiniz**:

📌 **İlk migration'ı oluşturun:**
```bash
alembic revision --autogenerate -m "Initial migration"
```

📌 **Migration'ı veritabanına uygulayın:**
```bash
alembic upgrade head
```

📌 **Yeni bir model veya sütun eklediğinizde:**
```bash
alembic revision --autogenerate -m "Updated models"
alembic upgrade head
```

---

## **API Kullanımı**

### **1. Kullanıcının Bakiyesini Görüntüleme**
- **GET /ledger/{owner_id}**

📌 **Örnek Yanıt:**
```json
{
    "success": true,
    "data": {
        "owner_id": "user123",
        "balance": 500
    }
}
```

---

### **2. Yeni Ledger Girişi Ekleme**
- **POST /ledger**

📌 **Örnek İstek:**
```json
{
    "owner_id": "user123",
    "operation": "CREDIT_ADD",
    "amount": 10,
    "nonce": "abc123"
}
```

📌 **Başarılı Yanıt:**
```json
{
    "success": true,
    "data": {
        "id": 12,
        "owner_id": "user123",
        "operation": "CREDIT_ADD",
        "amount": 10,
        "nonce": "abc123",
        "created_on": "2024-02-07T12:30:00"
    }
}
```

---

## **Faydalı Komutlar**

### **Docker Komutları**
- **Konteynerleri başlat:**  
  ```bash
  docker-compose up --build
  ```
- **Konteynerleri arka planda çalıştır:**  
  ```bash
  docker-compose up -d
  ```
- **Tüm servisleri durdur:**  
  ```bash
  docker-compose down
  ```
- **Çalışan servisleri görüntüle:**  
  ```bash
  docker ps
  ```
- **Docker loglarını takip et:**  
  ```bash
  docker-compose logs -f
  ```

### **Alembic (Migration) Komutları**
- **İlk migration'ı oluştur:**  
  ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```
- **Migration'ı uygula:**  
  ```bash
  alembic upgrade head
  ```
- **Son değişiklikleri geri al:**  
  ```bash
  alembic downgrade -1
  ```

---
