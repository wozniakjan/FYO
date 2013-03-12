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
            main_print_msg(file)
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
        end

        @flt = stack :width=>20, :height=>@widget_h do
            background yellow
            border white, :strokewidth=>3
        end
        @flt.click do
            return if @flt_lock
            size = @win_w/2 - 10
            coef = 10
            diff = (size/2-30)/coef
    
#            para "1 src:#{@src.width} dst:#{@dst.width} flt:#{@flt.width}\n" 

#            @flt_lock = true
            if(@flt.width < 30)
#                @a = animate (100) { |i|
#                    x = 1
#                    @dst.width -= coef
#                    @src.width -= coef 
#                    @flt.width += coef*2
#                    if i>diff
#                        @a.stop
#                        @flt_lock = false
#                    end
#                    para "src:#{@src.width} dst:#{@dst.width} flt:#{@flt.width}\n" 
#                }
                @src.width = 230
                @dst.width = 230
                @flt.width = 440
            else
#                @a = animate (100) { |i|
#                    x = 1
#                    @dst.width += coef
#                    @src.width += coef
#                    @flt.width -= coef*2
#                    if i>diff
#                        @a.stop
#                        @flt_lock = false
#                    end
#                }
                @src.width = 440
                @dst.width = 440
                @flt.width = 20
            end
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
#    def main_print_msg(msg)
#        @t1.text = msg 
#    end
end

