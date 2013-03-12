#Shoes.setup do
#    gem 'chunky_png'
#end
#
#load 'image_parsing.rb'

@@width = 900
@@height = 500

Shoes.app :title=>"FYO2013", :width=>@@width+2, :height=>@@height+2 do
    @win_w = @@width
    @win_h = @@height

    @widget_w = (@@width/2-10).to_i 
    @widget_h = @@height-25 

    @top_menu = flow :width=>@win_w do
        @open_button = stack :width=>(@win_w/3), :height=>25 do
            background blue
            border white, :strokewidth=>3
            para "image", :align=>'center', :stroke=>white
        end
        @open_button.click do
            file = ask_open_file
            display_image(file, @src)
            display_image(file, @dst)
            display_image(file, @flt)
        end

        @filter_button = stack :width=>(@win_w/3), :height=>25 do
            background green
            border white, :strokewidth=>3
            para "filter", :align=>'center', :stroke=>white
        end
        @filter_button.click do
        end

        @exit_button = stack :width=>(@win_w/3), :height=>25 do
            background black
            border white, :strokewidth=>3
            para "exit", :align=>'center', :stroke=>white
        end
        @exit_button.click do
            exit
        end
    end

    @pictures = flow :width=>@win_w do
        @src = stack :width=>@widget_w, :height=>@widget_h do
            background brown
            border white, :strokewidth=>3
            @src_image = image :hidden=>true do
            end
        end

        @flt = stack :width=>20, :height=>@widget_h do
            background yellow
            border white, :strokewidth=>3
        end
        @flt.click do
            return if @flt_lock

            @flt_lock = true
            if(@flt.width < 30)
                extend_filter_area()
            else
                shrink_filter_area()
            end
            @flt_lock = false
        end

        @dst = stack :width=>@widget_w, :height=>@widget_h do
            background purple
            border white, :strokewidth=>3
        end
    end

#    @error_console = flow do
#        @t1 = para ""
#    end
#    @error_console.height = 0
#
    def display_image(file, widget)
        widget.clear { 
            image file 
            border white, :strokewidth=>3
        }
    end

    def extend_filter_area()
        size = @win_w/2 - 10
        coef = 10
        diff = (size/2-30)/coef
#       @a = animate (100) { |i|
#           x = 1
#           @dst.width -= coef
#           @src.width -= coef 
#           @flt.width += coef*2
#           if i>diff
#               @a.stop
#               @flt_lock = false
#           end
#           para "src:#{@src.width} dst:#{@dst.width} flt:#{@flt.width}\n" 
#       }
        @src.width = 230
        @dst.width = 230
        @flt.width = 440
    end

    def shrink_filter_area()
        size = @win_w/2 - 10
        coef = 10
        diff = (size/2-30)/coef
#       @a = animate (100) { |i|
#           x = 1
#           @dst.width += coef
#           @src.width += coef
#           @flt.width -= coef*2
#           if i>diff
#               @a.stop
#               @flt_lock = false
#           end
#       }
        @src.width = 440
        @dst.width = 440
        @flt.width = 20
    end
end

