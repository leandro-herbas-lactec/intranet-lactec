import React from 'react';
import AreaInfoGrid from 'volto-lactec-intranet/components/AreaInfo/AreaInfoGrid';
import type { RelatedItem } from '@plone/types';

interface AreaGridItemProps {
  item: RelatedItem;
}

const AreaGridItem: React.FC<AreaGridItemProps> = (props) => {
  const { item } = props;
  return (
    <div className={`card-summary`}>
      <AreaInfoGrid content={item} icon />
    </div>
  );
};

export default AreaGridItem;
