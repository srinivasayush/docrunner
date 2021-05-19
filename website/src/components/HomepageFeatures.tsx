import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Easy Code Testing',
    // Svg: require('../../static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Docrunner allows you to easily test your code with a single command
      </>
    ),
  },
  {
    title: 'Focus on Writing Readable Documentation',
    // Svg: require('../../static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Docrunner takes care of the heavy lifting. <strong>You </strong> 
        can focus on writing expressive documentation for your readers
      </>
    ),
  },
  {
    title: 'Easy Configuration',
    // Svg: require('../../static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Use the <code>docrunner.toml</code> configuration file to easily manage your
        cli options
      </>
    ),
  },
];

function Feature({ title, description}) {
  // Add Svg as a  destructured parameter to use svg images in descriptions
  return (
    <div className={clsx('col col--4')}>
      {/* <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div> */}
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
