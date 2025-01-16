
# Multi-Threading in Python

A project demonstrating the implementation of **multi-threading** concepts in Python.  
This project showcases how to handle concurrent tasks effectively using Python's threading module.

---

## 📱 Features
- **Thread Creation**:  
  Learn how to create and start multiple threads.

- **Thread Synchronization**:  
  Manage shared resources using locks, semaphores, and condition variables.

- **Thread Communication**:  
  Use queues for safe data sharing between threads.

- **Real-World Examples**:  
  Examples like file reading, data processing, and web scraping with multi-threading.

- **Big Data Similarity Detection**:  
  Identifies similar records in large datasets using multi-threading to improve performance.

---

## 🔧 Technologies Used
- **Programming Language**: Python  
- **Libraries**: threading, queue  

---

## 🚀 How to Run the Project
1. Clone the repository:  
   ```bash
   git clone https://github.com/Ahmet-Sunaa/multi-threading-in-python.git
   ```

2. Navigate to the project directory:
   ```bash
   cd multi-threading-in-python
   ```

3. Run the desired Python script:
   ```bash
   python <script_name>.py
   ```

4. Follow the instructions in the script to observe multi-threading in action.

---

## 📂 Project Structure
- **`examples/`**: Contains various Python scripts demonstrating different multi-threading use cases.  
- **`resources/`**: Additional data files used for threading examples.  

---

## 🌟 Key Highlights
- **Concurrent Execution**: Perform multiple tasks simultaneously.
- **Resource Management**: Handle shared resources without conflicts.
- **Big Data Handling**: Analyze large datasets efficiently with multi-threading.
- **Similarity Detection**: Identify similar records based on word-level comparisons.

---

## 💡 Future Improvements
- Add examples for multi-threading in I/O-bound and CPU-bound tasks.
- Implement thread pooling for efficient thread management.
- Include case studies on optimizing performance using multi-threading.

---

## 📂 Additional Details from PDF
### Objective:
- **Reduce search time** in datasets using multi-threading.
- **Detect similarities** between records based on word-level comparisons.
- **Develop a desktop application** to filter and display results interactively.

### Dataset:
- Source: [Consumer Complaint Database](https://www.kaggle.com/datasets/selener/consumer-complaint-database)
- Structure:  
  - 6 columns: `Product`, `Issue`, `Company`, `State`, `Complaint ID`, `Zip Code`.
  - No null values.
  - Punctuation and stop words removed.

### Features to Implement:
1. Multi-threading for similarity detection.
2. Allow configurable **thread count** via the application interface.
3. Display:
   - Execution time per thread.
   - Total execution time.
4. Enable filtering based on similarity thresholds and columns.

### Example Scenarios:
- **Scenario 1**: Show records in the `Product` column with ≥ 60% similarity.
- **Scenario 2**: For similar `Product` records, display `Company` names with ≥ 70% similarity in `Issue`.
- **Scenario 3**: Display records with ≥ 50% similarity for `Complaint ID` = 3198084.
- **Scenario 4**: Use 5 threads to display records in the `Issue` column with ≥ 80% similarity.

---

# Python'da Çoklu İş Parçacığı (Multi-Threading)

Python'da **çoklu iş parçacığı** kavramlarının uygulanmasını gösteren bir proje.  
Bu proje, Python'un threading modülünü kullanarak eş zamanlı görevlerin nasıl verimli bir şekilde ele alınacağını gösterir.

---

## 📱 Özellikler
- **İş Parçacığı Oluşturma**:  
  Birden fazla iş parçacığı nasıl oluşturulur ve başlatılır öğrenin.

- **İş Parçacığı Senkronizasyonu**:  
  Paylaşılan kaynakları kilitler, semaforlar ve koşul değişkenleri kullanarak yönetin.

- **İş Parçacığı İletişimi**:  
  İş parçacıkları arasında güvenli veri paylaşımı için kuyrukları kullanın.

- **Gerçek Dünya Örnekleri**:  
  Dosya okuma, veri işleme ve çoklu iş parçacığıyla web kazıma gibi örnekler.

- **Büyük Veride Benzerlik Tespiti**:  
  Multithreading kullanarak büyük veri kümelerinde benzer kayıtları tespit edin.

---

## 🔧 Kullanılan Teknolojiler
- **Programlama Dili**: Python  
- **Kütüphaneler**: threading, queue  

---

## 🚀 Projeyi Çalıştırma
1. Depoyu klonlayın:  
   ```bash
   git clone https://github.com/Ahmet-Sunaa/multi-threading-in-python.git
   ```

2. Proje dizinine gidin:
   ```bash
   cd multi-threading-in-python
   ```

3. İstenilen Python scriptini çalıştırın:
   ```bash
   python <script_adi>.py
   ```

4. Çoklu iş parçacığının çalışmasını gözlemlemek için scriptteki talimatları izleyin.

---

## 📂 Proje Yapısı
- **`examples/`**: Farklı çoklu iş parçacığı kullanım durumlarını gösteren çeşitli Python scriptleri içerir.  
- **`resources/`**: İş parçacığı örnekleri için kullanılan ek veri dosyaları.  

---

## 🌟 Temel Vurgular
- **Eşzamanlı Yürütme**: Aynı anda birden fazla görevi yerine getirin.
- **Kaynak Yönetimi**: Çakışmalar olmadan paylaşılan kaynakları yönetin.
- **Büyük Veri Yönetimi**: Çoklu iş parçacığıyla büyük veri kümelerini verimli bir şekilde analiz edin.
- **Benzerlik Tespiti**: Kelime bazlı karşılaştırmalara dayalı olarak benzer kayıtları belirleyin.

---

## 📂 PDF'den Ek Bilgiler
### Amaç:
- Veri kümelerindeki **arama süresini azaltmak** için multi-threading kullanmak.
- Kayıtlar arasında **benzerlikleri tespit etmek**.
- Sonuçları filtrelemek ve masaüstü uygulamasında göstermek için bir arayüz geliştirmek.

### Veri Kümesi:
- Kaynak: [Consumer Complaint Database](https://www.kaggle.com/datasets/selener/consumer-complaint-database)
- Yapı:  
  - 6 sütun: `Product`, `Issue`, `Company`, `State`, `Complaint ID`, `Zip Code`.
  - Null değer içermemelidir.
  - Noktalama işaretleri ve durdurma kelimeleri kaldırılmalıdır.

### Geliştirme:
1. Benzerlik kontrolü için multi-threading kullanımı.
2. Uygulama arayüzünden **thread sayısının** seçilebilir olması.
3. Şunları ekranda gösterme:
   - Her thread'in çalışma süresi.
   - Toplam çalışma süresi.
4. Belirli sütunlar ve benzerlik oranlarına göre filtreleme.

### Örnek Senaryolar:
- **Senaryo 1**: `Product` sütununda %60 ve üzeri benzerlikteki kayıtları gösterin.
- **Senaryo 2**: Aynı `Product` için `Issue` sütununda %70 ve üzeri benzerliğe sahip `Company` adlarını gösterin.
- **Senaryo 3**: `Complaint ID` = 3198084 olan kayıt için %50 ve üzeri benzerlikteki kayıtları gösterin.
- **Senaryo 4**: 5 iş parçacığı ile `Issue` sütununda %80 ve üzeri benzerlikteki kayıtları gösterin.

---

## 🤵‍♂️ Geliştirici
- **Ahmet Sunaa**  
- [GitHub](https://github.com/Ahmet-Sunaa) üzerinden benimle iletişime geçin.
