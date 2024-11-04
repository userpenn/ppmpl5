from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tunggu antara 1 hingga 5 detik sebelum request

    # Mendapatkan semua hewan
    @task
    def get_hewan(self):
        self.client.get("/hewan")

    # Menambahkan hewan baru
    @task
    def add_hewan(self):
        self.client.post("/hewan", json={"name": "hewan baru", "species": "kucing", "age": 2})

    # Mendapatkan hewan berdasarkan ID
    @task
    def get_hewan_by_id(self):
        self.client.get("/hewan/1")

    # Memperbarui hewan berdasarkan ID
    @task
    def update_hewan(self):
        self.client.put("/hewan/1", json={"name": "hewan diperbarui", "species": "anjing", "age": 3})

    # Menghapus hewan berdasarkan ID
    @task
    def delete_hewan(self):
        self.client.delete("/hewan/1")