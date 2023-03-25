- **@pytest.mark.parametrize()**
> Test içeriğine parametreler göndemeye yarar.
```python
    @pytest.mark.parametrize("name, pass" , [("deneme , sifre")])
    def test_login(self, name, pass):
        pass
```

- **@pytest.mark.filterwarning()**
> Test e uyarı eklemek için kullanılır.
```python
    @pytest.mark.filterwarning("update var")
    def test_warning(self):
        update = True
        assert update == True
```

- **@pytest.mark.skipif()**
> Koşula uyuyorsa test pass geçilir.
```python
    a = 5
    @pytest.mark.skipif(a == 5)
    def test_skipif(self):
        pass
```

- **@pytest.mark.skip()**
> Test direkt pass geçilir.
```python
    @pytest.mark.skip(reason = "test geçildi")
    def test_skip(self):
        pass
```



