public class Utils {
    public static Double mean(Double[] data) {
        double sum = 0;
        for(Double number : data) {
            sum += number;
        }
        return sum/data.length;
    }

}
