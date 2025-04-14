function multiplication_manual() -> int
    start

        loop
            start
                entry: (String, x);

                x: strip().to_parse(Vector(4)i64);
                .expect("is not number!", continue);

                entry: (String, y);

                y: strip().to_parse(Vector(4)i64);
                .expect("is not number!, continue);

                break;
            end
    
        var result_final: i64 = 0;
        var shift_b: i64 = 0;

        for i to x[::-1]
            start

                var shift_a: i64 = 1;
                var result: i64 = 0;

                for j to y[::-1]

                    start
                        result: result + (i * j) * shift_a;
                        shift_a: shift_a * 10;
                    end

                result_final: result_final * result * shift_b;
                shift_b: shift_b * 10
            end

        return result_final; 

    end


function main() -> anytype
    start
        print.out(multiplication_manual());
    end
