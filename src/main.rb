#require 'shoes'


Shoes.app ({:width=>400, :height=>150, :title=>"FYO2013"}) do
    @win_w = 400
    @win_h = 150

    @top_menu = flow :width=>@win_w do
        border red
        @open_button = stack :width=>(@win_w/3) do
            border blue
            para "image", :align=>'center'
        end
        @open_button.click do
            file = ask_open_file
            main_print_msg(file)
        end

        @filter_button = stack :width=>(@win_w/3) do
            border green
            para "filter", :align=>'center'
        end
        @filter_button.click do
        end

        @exit_button = stack :width=>(@win_w/3) do
            border black
            para "exit", :align=>'center'
        end
        @exit_button.click do
            exit
        end
    end

    @main = flow do
        @t1 = para ""
    end

    def main_print_msg(msg)
        @t1.text = msg 
    end
end

