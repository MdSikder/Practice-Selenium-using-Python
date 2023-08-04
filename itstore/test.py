import scrapy
import os


class ITStoreSpider(scrapy.Spider):
    name = 'itstore'
    start_urls = ['https://www.itstore.qa/cisco-switches-doha-qatar/']

    def parse(self, response):
        # Create the folder to save the images
        save_folder = './images/'
        os.makedirs(save_folder, exist_ok=True)

        # Extract image URLs and download each image
        for img in response.css('img'):
            image_url = img.attrib['src']
            if not image_url.startswith('data:image'):  # Ignore base64 encoded images
                yield scrapy.Request(response.urljoin(image_url), self.save_image)

    def save_image(self, response):
        # Get the image filename from the URL
        filename = response.url.split('/')[-1]

        # Save the image to the specified folder
        save_path = os.path.join('./images', filename)
        with open(save_path, 'wb') as f:
            f.write(response.body)
