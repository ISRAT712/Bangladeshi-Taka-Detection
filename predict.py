import cv2
from model import model

def predict_image(image_path):

    results = model(image_path)

    predictions = []

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            predictions.append({
                "class": model.names[cls],
                "confidence": round(conf, 4),
                "bbox": [x1, y1, x2, y2]
            })

        annotated = result.plot()

        output_path = "outputs/output.jpg"

        cv2.imwrite(output_path, annotated)

    return predictions


if __name__ == "__main__":

    image = "test_images/test.jpg"

    preds = predict_image(image)

    print(preds)