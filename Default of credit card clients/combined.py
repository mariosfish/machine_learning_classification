def find_best_k(features, target, alpha=0.001, n_iter=10, n_clusters=2):
    scores = []
    n_features = len(features.columns)
    base_score = 0
    logreg = LogisticRegression(
            multi_class='auto', random_state=25, n_jobs=-1)
    # Main loop
    for kappa in range(1, n_features):
        
        X_new = SelectKBest(k=kappa).fit_transform(
            features, target)
        model = KMeans(n_clusters=n_clusters, random_state=25)
        sc = StandardScaler()
        sc.fit_transform(X_new)
        X_new = pd.DataFrame(X_new)
        X_new['cluster'] = model.fit_predict(X_new)
        X_train, X_test, y_train, y_test = train_test_split(
            X_new, y, test_size=0.3, random_state=25)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        logreg.fit(X_train, y_train)
        kappa_score = cross_val_score(logreg, X_new, y, cv=10).mean()
        scores.append(kappa_score)
        if kappa >= n_iter:
            if (abs(kappa_score-scores[-1])<alpha):
                print(scores)
                print(f'kappa: {scores.index(max(scores))+1} with score: {max(scores)}')
                break
            else:
                pass