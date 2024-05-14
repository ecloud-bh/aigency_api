# Aigency API Client Library

Aigency API Client Library, Aigency API ile kolay ve etkili bir şekilde etkileşim kurmanızı sağlar.

## Kurulum

Aşağıdaki adımları takip ederek kütüphaneyi kurabilirsiniz:

1. İndirdiğiniz klasöre giriş yapın:
    ```sh
    cd aigency_api
    ```

2. `README.md` dosyasını silin ve `Paket-README.md` dosyasının adını `README.md` olarak değiştirin:
    ```sh
    rm README.md
    mv Paket-README.md README.md
    ```

3. Bir sanal ortam (virtual environment) oluşturun ve aktif hale getirin:
    ```sh
    python -m venv env
    source env/bin/activate
    ```

4. Gerekli modülü yükleyin ve dosyaları paket haline getirin:
    ```sh
    pip install build
    python -m build
    ```

5. Paketi yüklemek için aşağıdaki komutu kullanın:
    ```sh
    pip install dist/aigency_api-0.1.0-py3-none-any.whl
    ```

## Kullanım

Komut satırında kütüphaneyi aşağıdaki gibi kullanabilirsiniz:

```sh
aigency_api
