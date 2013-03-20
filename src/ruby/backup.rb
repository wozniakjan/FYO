@@width = 800
@@height = 500

Shoes.app :title=>"FYO2013", :width=>@@width, :height=>@@height do
    @win_w = @@width
    @win_h = @@height-27
    @border_size = 3

    @top_menu = flow :width=>@win_w do
        @open_button = stack :width=>(@win_w/3), :height=>25 do
            background blue
            border white, :strokewidth=>@border_size
            para "image", :align=>'center', :border=>'white'
        end
        @open_button.click do
            file = ask_open_file
            main_print_msg(file)
        end

        @filter_button = stack :width=>(@win_w/3), :height=>25 do
            background green
            border white, :strokewidth=>@border_size
            para "filter", :align=>'center'
        end
        @filter_button.click do
        end

        @exit_button = stack :width=>(@win_w/3), :height=>25 do
            background black
            border white, :strokewidth=>@border_size
            para "exit", :align=>'center'
        end
        @exit_button.click do
            exit
        end
    end

    @pictures = flow :width=>@win_w do
        @src = stack :width=>(@win_w/2-10), :height=>@win_h do
            background brown
            border white, :strokewidth=>@border_size
        end

        @flt = stack :width=>20, :height=>@win_h do
            background yellow
            border white, :strokewidth=>@border_size
        end
        @flt.click do
            return if @flt_lock
            size = @win_w/2 - 10
            coef = 10
            diff = (size/2-10)/coef
                
            @flt_lock = true
            if(@flt.width < 30)
                @a = animate (100) {|i|
                    @src.width = @src.width - coef 
                    @flt.width = @flt.width + 2*coef
                    @dst.width = @dst.width - coef
                    if i>diff
                        @a.stop
                        @flt_lock = false
                    end
                }
            else
                @a = animate (100) {|i|
                    @src.width = @src.width + coef
                    @flt.width = @flt.width - 2*coef
                    @dst.width = @dst.width + coef
                    if i>diff
                        @a.stop
                        @flt_lock = false
                    end
                }
            end
        end

        @dst = stack :width=>(@win_w/2-12), :height=>@win_h do
            background purple
            border white, :strokewidth=>@border_size
        end
    end

#    @error_console = flow do
#        @t1 = para ""
#    end
#    @error_console.height = 0
#
#    def main_print_msg(msg)
#        @t1.text = msg 
#    end
end

