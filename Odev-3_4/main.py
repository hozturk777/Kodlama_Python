#       HTML : 
# Hiper Metin İşaretleme Dili (HTML, İngilizce HyperText Markup Language kelimelerinin baş harflerinin kısaltılmasıdır) web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir. Dilin son sürümü HTML5'tir.

#       HTML Locators :
#   -ID = ID, web sayfasında her öğeye özgü olduğu düşünülerek öğeleri bulmanın en yaygın yoludur.
#   -ClassName = ClassName locator, elementin class özelliği kullanılarak bulunmasını sağlar.
#   -Name = Selenium WebDriver’daki Name locator, ID gibi kullanılabilir.
#   -TagName = Selenium WebDriver’daki bu bulucu, div etiketi, etiket vb. gibi etiket adlarına sahip öğeleri tanımlamak için kullanılır.
#   -LinText = Elementler, bağlantı metni aracılığıyla yerleştirilebilir. Aynı metnin birden çok bağlantısının bulunduğu bir senaryoda, ilk bağlantı seçilir.
#   -CssSelector = Bir elementte ID ya da name ile ilgili bir bilgi yoksa veya bunlar değişken ise CSS selector ve Xpath ile elementi bulmaya çalışırız. Xpath ile karşılaştırıldığında CSS selector daha hızlı çalışmaktadır.
#   -XPath = Xpath, XML ifadelerini kullanarak web sayfasındaki öğeleri bulmaya yardımcı olur.
#   -DOM Locator = Elementi ID ve Name yoluyla DOM’un “getElementById” ve “getElementsByName” gibi yöntemlerini kullanarak tanımlayabiliriz. GetElementById yöntemi bir kerede yalnızca bir öğeyi bulur, diğer yöntem ise bu adla bulunan bir dizi elementi sağlamak için kullanılır. Bir dizi elementin olması durumunda belirtilen spesifik bir öğeye erişmek için index kullanabiliriz.

#       Selenium Methods :
#   get() = Bir websitesini açmak istediğinizde get methodu kullanılır.
#   title = Bir websitesine girdikten sonra, o sitenin meta title yani başlık etiketi içerisindeki metne ulaşmak isterseniz title methodu kullanılır.
#   back() = Bir websitesini açtıktan sonra, o sitede farklı sayfalara giriş yaptığınızı varsayalım, bir önceki sayfaya geri dönmek isterseniz back methodunu kullanmalısınız.
#   refresh() = Açtığınız bir sayfayı yenilemek isterseniz refresh methodunu kullanabilirsiniz.
#   close() && quit() = Bir websitesini açtıktan sonra, webdriver ile açılan tarayıcıda yeni bir sekme de açtığınızı düşünelim. Sadece şuan çalıştığınız sekmeyi kapatmak, ama tüm tarayıcıyı kapatmamak isterseniz o zaman close methodunu kullanmalısınız.Eğer kaç tane sekme var olursa olsun, tamamen komple tarayıcıyı kapatmak isterseniz o zaman quit methodunu kullanmalısınız.
#   maximize_window() = Açtığınız sayfayı tam ekran yapmak isterseniz maximize_window methodunu kullanabilirsiniz.
#   set_window_size(800, 600) = Eğer açtığınız sayfanın boyutlarını kendiniz belirlemek isterseniz (mesela 800 x 600) o zaman set_window_size methodunu kullanabilirsiniz.
#   save_screenshot() = Açtığınız sayfanın ekran görüntüsünü almak isterseniz o zaman kaydedilecek tam yol ve dosya ismi ile birlikte save_screenshot methodunu kullanmalısınız.
#   page_source = Açtığınız sayfanın kaynak koduna ulaşmak için ise page_source methodunu kullanmalısınız. Sayfa kaynağını aldıktan sonra bunu beautifulsoup gibi bir modüle aktarıp sonrasında istediğiniz yerleri keserek kendinize bir bot yazabilirsiniz.
#   find_element_by_id() = Html elemanının id bilgisini getirir.
#   find_element_by_class_name() = Html elemanının class ismini getirir.
#   find_element_by_css_selector() = Bazen bir html elemanını direkt olarak id veya css ile seçemeyebilirsiniz. Çünkü böyle bir öznitelik atanmamış olabilir. O zaman css selector kullanarak o elemana ulaşabilirsiniz.
#   find_element_by_name() = Html elemanının name bilgisini getirir.
#   find_element_by_xpath() = Html elemanının xpath bilgisini getirir.
#


