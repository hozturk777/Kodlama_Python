**- @pytest.mark.parametrize()**
> Test içeriğine parametreler göndemeye yarar.
```python
    @pytest.mark.parametrize("name, pass" , [("deneme , sifre")])
    def test_login(self, name, pass):
        pass
```
**- @pytest.mark.filterwarning()**
> Test e uyarı eklemek için kullanılır.
```python
    @pytest.mark.filterwarning("update var")
    def test_warning(self):
        update = True
        assert update == True
```

