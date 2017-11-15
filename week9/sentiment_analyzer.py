from nltk.corpus import movie_reviews 
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
 
# Extract features from the input list of words
def extract_features(words):
    return dict([(word, True) for word in words])
 
if __name__=='__main__':
    # Load the reviews from the corpus 
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')
     
    # Extract the features from the reviews
    features_pos = [(extract_features(movie_reviews.words(
            fileids=[f])), 'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(
            fileids=[f])), 'Negative') for f in fileids_neg]
     
    # Define the train and test split (80% and 20%)
    threshold = 0.8
    num_pos = int(threshold * len(features_pos))
    num_neg = int(threshold * len(features_neg))
     
     # Create training and training datasets
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]  

    # Print the number of datapoints used
    print('\nNumber of training datapoints:', len(features_train))
    print('Number of test datapoints:', len(features_test))
     
    # Train a Naive Bayes classifier 
    classifier = NaiveBayesClassifier.train(features_train)
    print('\nAccuracy of the classifier:', nltk_accuracy(
            classifier, features_test))

    N = 20
    print('\nTop ' + str(N) + ' most informative words:')
    for i, item in enumerate(classifier.most_informative_features()):
        print(str(i+1) + '. ' + item[0])
        if i == N - 1:
            break

    # Test input movie reviews
    input_reviews = [
        'Im not sure theres a single unsuccessful moment in this entire film. This was the movie that reminded me how much I can still love a movie. ', 
        'However, although entertaining in parts, there is very little connective tissue between the two main running storylines, creating a disappointing disconnect which prevents the movie from truly coming together in the end.',
        'While this has interesting moments, Foster seems unable to follow the story into as deep or dark a place as it should go and the ambiguity in the storytelling is unwarranted and frustrating to witness.', 
        'There is an appreciated sense of unconventionally to the film. However, the story quickly takes an overemotional and theatrical turn which diminish the many topics the story could have explored. ',
        "A sensational Korean trial makes for a fairly riveting cinematic ride, with its very own touches of that infamous gangnam style.",
        "Cross-dressing in the story is merely a tool for survival, but such border-crossing is inevitably rife with unintended consequences beyond narrative ones.",
        "Intent to Destroy goes well beyond the genre to build a terse, infuriating case against a monstrous injustice, one with frightening relevance to events today.",
        "Visual panache is enhanced by delightful voice talent from a widely diverse cast in a film with action, humor, and heart.",
        "Few of the characters have the first idea what might be coming next - nor do we, strapped into this feral shaggy dog story the Safdies have set rolling, hurtling towards their brilliant future.",
        "A warmhearted documentary that will tickle all audiences.",
        "Despite its flaws, Ask The Sexpert is a unique window into the inner lives of Mumbaikars in a way that narrative cinema seldom attempts."
    ]

    print("\nMovie review predictions:")
    for review in input_reviews:
        print("\nReview:", review)

        # Compute the probabilities
        probabilities = classifier.prob_classify(extract_features(review.split()))

        # Pick the maximum value
        predicted_sentiment = probabilities.max()

        # Print outputs
        print("Predicted sentiment:", predicted_sentiment)
        print("Probability:", round(probabilities.prob(predicted_sentiment), 2))

