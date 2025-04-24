package calculator;

public class CalculatorController {
    private final CalculatorModel model;
    private final CalculatorView view;

    public CalculatorController(CalculatorModel model, CalculatorView view) {
        this.model = model;
        this.view = view;
    }

    public void run() {
        try {
            String expression = view.getExpression();
            double result = model.evaluate(expression);
            view.showResult(result);
        } catch (Exception e) {
            view.showError(e.getMessage());
        }
    }
}
