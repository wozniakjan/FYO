require 'chunky_png'

class Pictures
    def initialize(file)
        @src = ChunkyPNG::Image.from_file(file)
        @src.save("test.png")
    end
end

Pictures.new("lena.png")
